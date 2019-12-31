from django.db import models

# Create your models here.

class student(models.Model):
    student_id = models.CharField(max_length=20)
    courses_code = models.CharField(max_length=8,default="")
    def __str__(self):
        return self.student_id