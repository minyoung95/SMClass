from django.db import models

# Create your models here.
## 오라클에서 table 생성가능, insert,update,select,delete,create
## 오라클 접속하지 않고 table 생성가능 : ORM(Object Relational Mapping - 객체 관계형 매핑) 방식 - sql구문 필요 x

# 객체 선언 > sql 구문을 알아서 만들어줌
class Students(models.Model):
  s_name = models.CharField(max_length=100)
  s_major = models.CharField(max_length=100) # varchar2(100)
  s_age = models.IntegerField(default=0) # number default 0
  s_grade = models.IntegerField(default=0)
  s_gender = models.CharField(max_length=30)
  
  def __str__(self):
    return self.s_name