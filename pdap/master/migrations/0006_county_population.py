# Generated by Django 3.2 on 2021-04-29 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0005_county_state_iso'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='population',
            field=models.IntegerField(null=True),
        ),
    ]
