# Generated by Django 3.0.1 on 2019-12-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0009_auto_20191229_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.CharField(default='', max_length=20),
        ),
    ]