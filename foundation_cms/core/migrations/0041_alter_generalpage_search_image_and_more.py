# Generated by Django 4.2.20 on 2025-07-30 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0001_initial"),
        ("core", "0040_alter_generalpage_body_alter_homepage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generalpage",
            name="search_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Image must be high quality, include our logo mark and have the dimensions 1200 x 628 px. For more design guidelines see here: https://foundation.mozilla.org/en/docs/brand/brand-identity/social-media/#og-images",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.foundationcustomimage",
                verbose_name="Search image",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="search_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Image must be high quality, include our logo mark and have the dimensions 1200 x 628 px. For more design guidelines see here: https://foundation.mozilla.org/en/docs/brand/brand-identity/social-media/#og-images",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.foundationcustomimage",
                verbose_name="Search image",
            ),
        ),
    ]
