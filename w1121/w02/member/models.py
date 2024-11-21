from django.db import models

# Create your models here.
class Member(models.Model):
  id = models.CharField(max_length=50,primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  nicName = models.CharField(max_length=100)
  tel = models.CharField(max_length=100,default='010-1111-1111')
  gender = models.CharField(max_length=30,default='남자')
  mdate = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f'{self.id},{self.name},{self.nicName}'