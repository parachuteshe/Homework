# Generated by Django 3.0.1 on 2019-12-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(default='暂无描述')),
                ('notification', models.TextField(default='暂无公告')),
                ('reference', models.TextField(default='暂无参考')),
                ('code', models.CharField(default='', max_length=8, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
