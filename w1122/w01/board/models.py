from django.db import models

# Create your models here.
class Board(models.Model):
  bno = models.AutoField(primary_key=True) # AutoField : 자동 번호 // 게시판 번호
  id = models.CharField(max_length=100)
  # member = models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True) # primary_key와 상관없이 삭제? 적용 
  btitle = models.CharField(max_length=1000) # 글 제목
  bcontent = models.TextField() # 글 내용
  bgroup = models.IntegerField(null=True) # 답글 사용할 때 그룹을 지어줌
  bstep = models.IntegerField(default=0) # 답글 사용할 때 순서
  bindent = models.IntegerField(default=0) # 답글 사용할 때 들여쓰기
  bhit = models.IntegerField(default=0) # 조회수
  bdate = models.DateTimeField(auto_now=True) # 글쓴 날짜
  # btop : 공지글 같은거 쓸때 우선순위가 가장 높게 올라갈 수 있게 (상단고정?) 만들어줌
  
  def __str__(self):
    return f'{self.bno},{self.id},{self.btitle},{self.bdate}'