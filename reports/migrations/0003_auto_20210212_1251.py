# Generated by Django 3.1.6 on 2021-02-12 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20210212_0803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('-scan_date',), 'verbose_name_plural': 'Reports'},
        ),
    ]
