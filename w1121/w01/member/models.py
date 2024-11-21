from django.db import models

# Create your models here.
class Member(models.Model):
  id = models.CharField(max_length=50,primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=50)
  nicName = models.CharField(max_length=50)
  tel = models.CharField(max_length=50,default='010-1111-1111')
  gender = models.CharField(max_length=10,default='남자')
  hobby = models.CharField(max_length=50,default='game')
  mdate = models.DateTimeField(auto_now=True) # auto_now_add : 입력할 때 시간설정 이후 변경x // auto_now : 수정할 때 갱신됨
  
  def __str__(self): # 위 테이블을 불러올때 보이는 부분
    return f'{self.id},{self.name},{self.nicName}'