# Generated by Django 3.0.1 on 2019-12-29 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0007_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
