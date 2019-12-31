from django.db import models

# Create your models here.
#编辑 models.py 文件，改变模型。
#运行 python manage.py makemigrations 为模型的改变生成迁移文件。
#运行 python manage.py migrate 来应用数据库迁移。

class Course(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(default="No description yet.")
    notification = models.TextField(default="No notification yet.")
    reference = models.TextField(default="No reference yet.")
    code = models.CharField(max_length=8,unique=True,default="")
    user = models.CharField(max_length=20,default="")
    def __str__(self):
        return self.name

# class Class(models.Model):
#     course_id = models.CharField(max_length=20,unique=True)
#     week = models.CharField(max_length=20,unique=True)
#     class_description = models.TextField(default="No description yet.")
#     course_files = 
#     def __str__(self):
#             return self.week

# class  Assignment(models.Model):
#     class_id = models.CharField(max_length=20,unique=True)
#     homework_name = models.CharField(max_length=20,unique=True)
#     homework_requirement = models.TextField(default="No requirement yet.")
#     modify_time = models.DateTimeField(auto_now = True)
#     due_date = models.DateTimeField(default=timezone.now())
#     homework_files = 
#     def __str__(self):
#             return self.homework_name
    
