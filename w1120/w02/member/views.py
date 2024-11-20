from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def mlist(request):
  return render(request,'mlist.html')

def cookWrite(request):
  response = render(request,'cookWrite.html')
  if request.method == 'GET':
    print('GET 방식으로 들어옴')
  else:
    print('POST방식으로 들어옴')
    response = render(request,'index.html')
    ckey = request.POST.get('ckey')
    cvalue = request.POST.get('cvalue')
    response.set_cookie(ckey,cvalue)
  return response

def cookDelete(request):
  if request.method == 'GET':
    response = render(request,'cookDelete.html')
    return response
  else:
    pass

def login(request):
  if request.method =="GET":
    response = render(request,'login.html')
  else:
    emsg = ''
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    
    qs = Member.objects.filter(id=id,pw=pw) # 찾기
    if qs: # qs가 있으면
      context ={'emsg':emsg,'member':qs[0]}
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName
      response = render(request,'index.html',context)
    else:
      emsg = '아이디 또는 패스워드가 일치하지 않습니다.'
      context ={'emsg':emsg,'member':''}
      response = render(request,'login.html',context)
  return response
## render 이동을 해도 url링크가 처음 값과 같음(url이 바뀌지 않음)
## 페이지가 바뀔때는 redirect 쓰는게 좋음 update delete
def logout(request):
  request.session.clear()  # 세션 모두삭제
  # del request.session['session_id'] # 해당 세션만 삭제
  return redirect('index')