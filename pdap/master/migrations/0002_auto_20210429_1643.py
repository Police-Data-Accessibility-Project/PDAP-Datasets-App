# Generated by Django 3.2 on 2021-04-29 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'verbose_name_plural': 'Agencies'},
        ),
        migrations.AlterModelOptions(
            name='agency_type',
            options={'verbose_name_plural': 'Agency Types'},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name_plural': 'Counties'},
        ),
        migrations.AlterModelOptions(
            name='data_type',
            options={'verbose_name_plural': 'Data Types'},
        ),
        migrations.AlterModelOptions(
            name='format_type',
            options={'verbose_name_plural': 'Format Types'},
        ),
        migrations.AlterModelOptions(
            name='source_type',
            options={'verbose_name_plural': 'Source Types'},
        ),
        migrations.AlterModelOptions(
            name='update_frequency',
            options={'verbose_name_plural': 'Update Frequencies'},
        ),
    ]
