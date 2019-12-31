# Generated by Django 2.2.7 on 2019-12-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20191229_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('courses_code', models.CharField(default='', max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(default='暂无描述')),
                ('notification', models.TextField(default='暂无公告')),
                ('reference', models.TextField(default='暂无参考')),
                ('code', models.CharField(default='', max_length=8, unique=True)),
                ('teacher_id', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('psw', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('identity', models.CharField(default='学生', max_length=2)),
            ],
        ),
    ]