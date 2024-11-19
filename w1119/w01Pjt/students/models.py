from django.db import models

# Create your models here.
class Student(models.Model):
  ## primary key가 없으면 자동으로 pk=id 생성
  name = models.CharField(max_length=100)
  major = models.CharField(max_length=100)
  grade = models.IntegerField(default=0)
  age = models.IntegerField(default=0)
  gender = models.CharField(max_length=10)
  hobby = models.CharField(max_length=30)
  
  def __str__(self):
    return f"{self.name},{self.major},{self.grade}"