# Generated by Django 3.1.5 on 2021-01-21 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_contactpage_formfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='page',
        ),
    ]