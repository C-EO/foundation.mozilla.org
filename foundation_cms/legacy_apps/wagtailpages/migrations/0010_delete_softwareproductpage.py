# Generated by Django 3.2.12 on 2022-03-28 22:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
        ("wagtailinventory", "0002_pageblock_unique_constraint"),
        ("wagtailforms", "0004_add_verbose_name_plural"),
        ("wagtail_footnotes", "0005_alter_footnote_locale_alter_footnote_translation_key"),
        ("wagtailredirects", "0007_add_autocreate_fields"),
        ("wagtailpages", "0009_auto_20220325_1735"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SoftwareProductPage",
        ),
    ]
