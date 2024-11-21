from django.shortcuts import render, redirect
from member.models import Member

def login(request):
  if request.method == 'GET':
    return render(request,'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw) # Member에 있는 id와 pw가 입력한 것과 같은지 확인
    if qs:
      msg = '로그인 되었습니다.'
      print(msg)
      ## 세션연결
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName
      return redirect('index') # 로그인되면 메인페이지로(앱이름)
    else:
      msg = '아이디 또는 패스워드가 일치하지 않습니다.'
      print(msg)
      return render(request,'login.html',{'login_msg':msg})
    
def logout(request):
  request.session.clear() # 전체세션 삭제
  # del request.session['session_id'] 해당 세션 삭제
  return redirect('/') # url

def mlist(request):
  id = request.session['session_id']
  if id == 'admin':
    qs = Member.objects.all() # 다 볼수 있게
  else:
    qs = Member.objects.filter(id=id) # 자기꺼만 볼수 있게?
  context = {'mlist':qs}
  return render(request,'mlist.html',context)

def mview(request,id):
  print('아이디 : ',id)
  qs = Member.objects.filter(id=id)
  context = {'mem':qs[0]}
  return render(request,'mview.html',context)

def mwrite(request):
  if request.method == 'GET':
    return render(request,'mwrite.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    nicName = request.POST.get('nicName')
    tel = request.POST.get('tel')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)
    
    qs = Member(id=id,pw=pw,name=name,nicName=nicName,tel=tel,gender=gender,hobby=hobby)
    qs.save()
    return redirect('member:mlist')
  
def mupdate(request,id):
  if request.method == 'GET':
    print('회원정보 : ',id)
    qs = Member.objects.filter(id=id)
    context = {'mem':qs[0]}
    return render(request,'mupdate.html',context)
  else:
    id = request.session['session_id'] # admin이 아닌 경우 세션을 사용하여 저장
    if request.session['session_id'] == 'admin': # 관리자로그인 일땐 id를 가져와서 저장
      id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    nicName = request.POST.get('nicName')
    tel = request.POST.get('tel')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)
    
    qs = Member.objects.get(id=id)
    
    qs.pw = pw
    qs.name = name
    qs.nicName = nicName
    qs.tel = tel 
    qs.gender = gender
    qs.hobby = hobby
    qs.save()
    
    
    return redirect('member:mlist')

def mdelete(request,id):
  print('회원정보 : ',id)
  Member.objects.get(id=id).delete()
  # return render(request,'mlist.html') 기존 형태로 돌아갔을 때 주소창이 그대로여서 계속 삭제될 위험이 있음
  return redirect('member:mlist')