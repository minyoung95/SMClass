from django.shortcuts import render
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
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName
      context = {'lmsg':'1'}
      return render(request,'login.html',context)
    else:
      context = {'lmsg':'0'}
      return render(request,'login.html',context)
    
def logout(request):
  request.session.clear() # del request.session[session_id] 1개 삭제
  context = {'lmsg':'1'}
  return render(request,'index.html',context)