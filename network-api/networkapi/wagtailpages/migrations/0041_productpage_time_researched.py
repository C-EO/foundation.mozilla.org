# Generated by Django 3.1.11 on 2021-10-01 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0040_auto_20210929_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpage',
            name='time_researched',
            field=models.PositiveIntegerField(default=0, help_text='How many hours were spent researching this product?'),
        ),
    ]
