# Generated by Django 2.2.7 on 2019-12-29 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign1', '0003_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_reg',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='student_reg',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
