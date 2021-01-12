from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

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

    content_panels = Page.content_panels + [
        FieldPanel('project_name', classname="full"),
        FieldPanel('project_tagline'),
        ImageChooserPanel('cover'),
        FieldPanel('about_text_left'),
        FieldPanel('about_text_right'),
    ]
