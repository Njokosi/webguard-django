# Generated by Django 3.1.6 on 2021-02-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20210212_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='scan_date'),
        ),
    ]
