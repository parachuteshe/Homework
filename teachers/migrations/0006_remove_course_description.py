# Generated by Django 3.0.1 on 2019-12-27 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_auto_20191228_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
    ]
