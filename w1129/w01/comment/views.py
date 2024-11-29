from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입
from member.models import Member
from board.models import Board
from comment.models import Comment


def cwrite(request):
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get('bno',1)
  board = Board.objects.get(bno=bno)
  cpw = request.POST.get('cpw','')
  ccontent = request.POST.get('ccontent','')
  print('확인 : ',cpw,ccontent)
  
  qs = Comment.objects.create(member=member,board=board,cpw=cpw,ccontent=ccontent)
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print('확인 : ',list_qs)
  context = {'result':'success','comment':list_qs}
  return JsonResponse(context)

def cdelete(request):
  cno = request.POST.get('cno')
  print('확인 : ',cno)
  Comment.objects.get(cno=cno).delete()
  context = {'result':'success'}
  return JsonResponse(context)

def cupdate(request):
  id = request.session['session_id']
  cno = request.POST.get('cno',1)
  ccontent = request.POST.get('ccontent','')
  print('확인 : ',cno,ccontent)
  
  qs = Comment.objects.get(cno=cno)
  qs.ccontent = ccontent
  qs.save()
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print('확인 : ',list_qs)
  context = {'result':'success','comment':list_qs}
  return JsonResponse(context)