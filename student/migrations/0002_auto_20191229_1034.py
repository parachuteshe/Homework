# Generated by Django 2.2.7 on 2019-12-29 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='item_num',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='courses',
            name='week_num',
            field=models.IntegerField(default=1),
        ),
    ]