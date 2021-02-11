from django.conf import settings
from django.core.mail import EmailMessage
from django.template.defaultfilters import pluralize

from wagtailstreamforms.hooks import register

import smtplib, ssl

from decouple import config

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "rachel.development@gmail.com"  # Enter your address, must be gmail
password = config('EMAIL_PASSWORD')

context = ssl.create_default_context()

@register('process_form_submission')
def email_submission(instance, form):
    """ Send an email with the submission. """

    addresses = [instance.advanced_settings.to_address]
    content = ['Subject: New Contact Form Submission\n', ]
    from_address = settings.DEFAULT_FROM_EMAIL

    # build up the email content
    for field, value in form.cleaned_data.items():
        if field in form.files:
            count = len(form.files.getlist(field))
            value = '{} file{}'.format(count, pluralize(count))
        elif isinstance(value, list):
            value = ', '.join(value)
        content.append('{}: {}'.format(field, value))
    content = '\n'.join(content)

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, addresses, content)