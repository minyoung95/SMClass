from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입
from member.models import Member

# Create your views here.
def login(request):
  return render(request,'login.html')

def loginChk(request):
  id = request.POST.get('id','')
  pw = request.POST.get('pw','')
  print('확인 : ',id,pw)
  qs = Member.objects.filter(id=id,pw=pw)
  
  if qs:
    request.session['session_id'] = qs[0].id
    request.session['session_nicName'] = qs[0].nicName
    list_qs = list(qs.values())
    context = {'result':'success','member':list_qs}
  else:
    context = {'result':'fail'}
  return JsonResponse(context)

def logout(request):
  request.session.clear()
  return redirect('/')