# Generated by Django 2.0 on 2019-01-20 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='grade',
            field=models.ManyToManyField(to='grades.Grade'),
        ),
    ]