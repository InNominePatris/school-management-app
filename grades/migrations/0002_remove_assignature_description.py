# Generated by Django 2.0 on 2019-01-16 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignature',
            name='description',
        ),
    ]