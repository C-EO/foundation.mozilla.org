# Generated by Django 3.1.11 on 2021-09-23 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0037_auto_20210923_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banneredcampaignpage',
            name='cta',
        ),
        migrations.RemoveField(
            model_name='campaignpage',
            name='cta',
        ),
    ]
