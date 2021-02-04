# Generated by Django 3.1.5 on 2021-02-04 11:38

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtailstreamforms.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210204_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='contact_body',
            field=wagtail.core.fields.StreamField([('form', wagtail.core.blocks.StructBlock([('form', wagtailstreamforms.blocks.FormChooserBlock()), ('form_action', wagtail.core.blocks.CharBlock(help_text='The form post action. "" or "." for the current page or a url', required=False)), ('form_reference', wagtailstreamforms.blocks.InfoBlock(help_text='This form will be given a unique reference once saved', required=False))]))], blank=True),
        ),
    ]
