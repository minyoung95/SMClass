from django.db import models
from member.models import Member

# Create your models here.
class Board(models.Model):
  bno = models.AutoField(primary_key=True) # AutoField : 자동을 번호증가
  # id = models.CharField(max_length=100)
  ### ForeignKey : primarykey에 등록이 되어있지 않은 데이터로 작성하려고 하면 에러
  ## on_delete : CASCADE - 부모지울때 자식도 다 지움, SET_NULL - 부모를 지우면 자식 내용 null처리
  ## DO_NOTHING : 부모,자식 상관없이 삭제 가능
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=True) 
  btitle = models.CharField(max_length=1000)
  bcontent = models.TextField() # TextField : 대용량
  ## 계층형 게시판
  bgroup = models.IntegerField(null=True)
  bstep = models.IntegerField(default=0)
  bindent = models.IntegerField(default=0)
  bhit = models.IntegerField(default=0)
  bdate = models.DateTimeField(auto_now=True)
  ## img 파일업로드
  bfile = models.ImageField(null=True,upload_to='board') # 이미지 유형(upload_to : 파일저장위치)
  # bimg = models.FileField(null=True) # 전체파일 유형
  
  def __str__(self):
    return f'{self.bno},{self.btitle},{self.bgroup},{self.bdate}'