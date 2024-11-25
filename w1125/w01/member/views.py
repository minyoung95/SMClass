from django.shortcuts import render,redirect
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
      request.session['session_id'] = qs[0].id
      request.session['session_nicName'] = qs[0].nicName
      context = {'lmsg':'1'}
    else:
      context = {'lmsg':'0'}
      
    return render(request,'login.html',context)

def logout(request):
  request.session.clear()
  return redirect('/')