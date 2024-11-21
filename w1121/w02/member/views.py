from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def login(request):
  if request.method == 'GET':
    return render(request,'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
      msg = '로그인이 되셨습니다.'
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName
      return redirect('index')
    else:
      msg = '아이디 또는 패스워드가 일치하지 않습니다.'
      return render(request,'login.html',{'login_msg':msg})

def logout(request):
  request.session.clear() # 세션전체삭제
  return redirect('/')

def join01(request):
  return render(request,'join01.html')

def join02(request):
  return render(request,'join02.html')