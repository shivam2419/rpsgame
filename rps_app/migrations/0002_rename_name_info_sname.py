# Generated by Django 4.2.6 on 2023-11-06 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rps_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='name',
            new_name='sname',
        ),
    ]
