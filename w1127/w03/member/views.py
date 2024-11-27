from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from member.models import Member

# Create your views here.
def login(request):
  return render(request,'login.html')

### ajax 통신
# @csrf_exempt
def loginChk(request):
  id = request.POST.get('id','')
  pw = request.POST.get('pw','')
  print('html에서 넘어온 데이터 : ',id, pw)
    
  ###### filter 검색######
  ## 객체보내기 (리스트타입으로)
  qs = list(Member.objects.filter(id=id,pw=pw).values())
  if qs:
    context = {'member':qs,'result':'success'}
  else:
    context = {'result':'fail'}
    
  ## 변수보내기
  # if qs:
  #   context = {'id':qs[0].id,'nicName':qs[0].nicName,'result':'success'}
  # else:
  #   context = {'result':'fail'}
  #######################
  return JsonResponse(context)

def join01(request):
  return render(request,'join01.html')

def join02(request):
  return render(request,'join02.html')

# Ajax 통신
def idChk(request):
  id = request.POST.get('id')
  print('id : ',id)
  context = {'id':id,'result':'success'}
  return JsonResponse(context)