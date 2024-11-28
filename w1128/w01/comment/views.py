from django.shortcuts import render
from member.models import Member
from board.models import Board
from comment.models import Comment
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers # json타입

# Create your views here.
def clist(request):
  return

def cwrite(request):
  ## 데이터 가져오기
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get('bno',1)
  board = Board.objects.get(bno=bno)
  cpw = request.POST.get('pw','') # 비밀댓글이 아닐시 ''
  ccontent = request.POST.get('ccontent','')
  print(cpw,ccontent)
  
  ## 데이터 저장
  qs = Comment.objects.create(board=board,member=member,ccontent=ccontent,cpw=cpw)
  json_qs = serializers.serialize('json',[qs]) # get으로 가져오면 serialize
  context = {'comment':json_qs, 'result':'success'}
  return JsonResponse(context)