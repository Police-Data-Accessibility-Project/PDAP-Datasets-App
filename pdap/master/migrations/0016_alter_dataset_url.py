# Generated by Django 3.2.2 on 2021-06-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0015_alter_agency_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
