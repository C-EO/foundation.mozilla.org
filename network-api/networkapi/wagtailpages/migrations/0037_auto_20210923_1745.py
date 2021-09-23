# Generated by Django 3.1.11 on 2021-09-23 17:45

from django.db import migrations, models
import django.db.models.deletion


def copy_cta_to_petition_cta(apps, schema_editor):
    models = [
        apps.get_model("wagtailpages", "CampaignPage"),
        apps.get_model("wagtailpages", "BanneredCampaignPage"),
    ]

    for Model in models:
        for page in Model.objects.all():
            if page.cta:
                page.petition_cta = page.cta
                page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0036_blogpagecategory_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='banneredcampaignpage',
            name='petition_cta',
            field=models.ForeignKey(blank=True, help_text='Choose an existing, or create a new, pettition form', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='banner_page_for_petition', to='wagtailpages.petition'),
        ),
        migrations.AddField(
            model_name='campaignpage',
            name='petition_cta',
            field=models.ForeignKey(blank=True, help_text='Choose existing or create new sign-up form', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='campaign_page_for_petition', to='wagtailpages.petition'),
        ),
        migrations.RunPython(
            code=copy_cta_to_petition_cta
        ),
    ]
