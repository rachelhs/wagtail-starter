# Generated by Django 3.1.5 on 2021-01-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_about_text_right'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='team_text_left',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='homepage',
            name='team_text_right',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
