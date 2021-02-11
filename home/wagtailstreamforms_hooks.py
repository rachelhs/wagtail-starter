from django.conf import settings
from django.core.mail import EmailMessage
from django.template.defaultfilters import pluralize

from wagtailstreamforms.hooks import register

import smtplib, ssl

from decouple import config

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "rachel.development@gmail.com"  # Enter your address
receiver_email = "rachelsmith400@hotmail.co.uk"  # Enter receiver address
password = config('EMAIL_PASSWORD')
message = """\
Subject: Hi there
This message is sent from Python."""

context = ssl.create_default_context()

@register('process_form_submission')
def email_submission(instance, form):
    """ Send an email with the submission. """

    addresses = [instance.advanced_settings.to_address]
    content = ['Please see below submission\n', ]
    from_address = settings.DEFAULT_FROM_EMAIL
    subject = 'New Form Submission : %s' % instance.title

    # build up the email content
    for field, value in form.cleaned_data.items():
        if field in form.files:
            count = len(form.files.getlist(field))
            value = '{} file{}'.format(count, pluralize(count))
        elif isinstance(value, list):
            value = ', '.join(value)
        content.append('{}: {}'.format(field, value))
    content = '\n'.join(content)

    # create the email message
    email = EmailMessage(
        body=content,
        from_email=from_address,
        to=addresses
    )

    # attach any files submitted
    for field in form.files:
        for file in form.files.getlist(field):
            file.seek(0)
            email.attach(file.name, file.read(), file.content_type)

    # finally send the email
    #email.send(fail_silently=True)

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, addresses, content)