from django.db import models

from wagtail.core.models import Page
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel, PageChooserPanel)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (AbstractEmailForm, AbstractFormField)
from wagtailcaptcha.models import WagtailCaptchaEmailForm

from modelcluster.fields import ParentalKey

class HomePage(Page):
    project_name = models.CharField(max_length=255, blank=True,)
    project_tagline = models.CharField(max_length=255, blank=True,)
    cover = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    about_text_left = models.CharField(max_length=500, blank=True,)
    about_text_right = models.CharField(max_length=500, blank=True,)
    team_text_left = models.CharField(max_length=500, blank=True,)
    team_text_right = models.CharField(max_length=500, blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel('project_name', classname="full"),
        FieldPanel('project_tagline', classname="full"),
        ImageChooserPanel('cover'),
        FieldPanel('about_text_left', classname="full"),
        FieldPanel('about_text_right', classname="full"),
        FieldPanel('team_text_left', classname="full"),
        FieldPanel('team_text_right', classname="full"),
    ]
