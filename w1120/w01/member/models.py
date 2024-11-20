from django.db import models
import datetime

# Create your models here.
class Member(models.Model):
  id = models.CharField(max_length=50, primary_key=True) # null x, 동일한 값 x
  pw = models.CharField(max_length=100, blank=False) # 빈칸 x
  name = models.CharField(max_length=100)
  nicname = models.CharField(max_length=100)
  cdate = models.DateTimeField(auto_now=True) # 자동으로 현재시간 입력
  
  def __str__(self):
    return f"{self.id},{self.name}"