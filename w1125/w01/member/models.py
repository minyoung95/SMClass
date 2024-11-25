from django.db import models
import datetime
# from datetime import datetime >> datetime 한번만 적어도 된다.

# Create your models here.
class Member(models.Model):
  id = models.CharField(max_length=50,primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  nicName = models.CharField(max_length=100)
  tel = models.CharField(max_length=20,default='010-0000-0000')
  gender = models.CharField(max_length=10,default='남자')
  hobby = models.CharField(max_length=30,default='game')
  mdate = models.DateTimeField(auto_now=True) # 입력 시 갱신
  # mdate = models.DateTimeField(default=datetime.datetime.now()) # datetime 클래스 안의 datetime 함수
  
  def __str__(self): # 앞의 데이터들을 나타내려면 self. 을 붙여야함
    return f'{self.id},{self.name},{self.mdate}'