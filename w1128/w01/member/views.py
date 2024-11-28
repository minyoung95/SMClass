from django.shortcuts import render
from member.models import Member
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers # json타입

## 로그인
# @csrf_exempt : 예외처리
def login(request):
  return render(request,'login.html')

def logout(request):
  request.session.clear()
  context = {"outmsg":"1"}
  return render(request,'index.html',context)

def loginChk(request):
  id = request.POST.get('id','')
  pw = request.POST.get('pw','')
  # qs = Member.objects.get(id=id,pw=pw) # qs:set >> list타입으로 변경
  qs = Member.objects.filter(id=id,pw=pw)
  if qs:
    request.session['session_id'] = id
    request.session['session_nicName'] = qs[0].nicName
    # json_qs = serializers.serialize('json',[qs]) # json타입 변경
    # context = {'result':'success','member':json_qs}
    qs_list = list(qs.values())
    context = {'result':'success','member':qs_list}
  else:
    context = {'result':'fail'}
  return JsonResponse(context)

def step03(request):
  return render(request,'step03.html')

def idChk(request):
  id = request.POST.get('id','')
  
  qs = Member.objects.filter(id=id)
  qs_list = list(qs.values())
  if not qs:
    context = {'result':'success'}
  else:
    context = {'result':'fail','member':qs_list}
  return JsonResponse(context)