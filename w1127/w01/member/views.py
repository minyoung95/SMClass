from django.shortcuts import render
from member.models import Member

# Create your views here.
def login(request):
  if request.method == 'GET':
    # cookId = request.COOKIES.get('cookId','')
    # context = {'cookId':cookId}
    return render(request,'login.html',context)
  else:
    # response = render(request,'login.html')
    
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    # saveId = request.POST.get('saveId')
    
    qs = Member.objects.filter(id=id,pw=pw)
    
    # if saveId is not None:
    #   response.set_cookie('cookId',id,max_age=60*60)
    # else:
    #   response.delete_cookie('cookId')
    
    if qs:
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName
      context = {'lmsg':'1'}
      return render(request,'login.html',context)
    else:
      context = {'lmsg':'0'}
      return render(request,'login.html',context)
  
def logout(request):
  request.session.clear()
  context = {'lmsg':'1'}
  return render(request,'index.html',context)
      