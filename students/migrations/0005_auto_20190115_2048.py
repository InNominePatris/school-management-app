# Generated by Django 2.0 on 2019-01-16 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20190115_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='first_name',
            field=models.CharField(editable=False, max_length=50),
        ),
    ]
