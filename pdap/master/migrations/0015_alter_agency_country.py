# Generated by Django 3.2.2 on 2021-06-13 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0014_auto_20210609_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='country',
            field=models.CharField(default='US', max_length=2, null=True),
        ),
    ]
