# Generated by Django 3.2 on 2021-05-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0008_rename_scraper_id_dataset_scraper'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
