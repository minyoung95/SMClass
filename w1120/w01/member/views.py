from django.shortcuts import render
from member.models import Member

# Create your views here.

## 회원 전체 리스트
def mlist(request):
  qs = Member.objects.all()
  context = {'mlist':qs}
  return render(request,'mlist.html',context)

## 로그인
def login(request):
  if request.method == 'GET': # 로그인페이지를 들어왔을 떄
    print('쿠키정보 : ',request.COOKIES.get('cookinfo'))
    saveId = request.COOKIES.get('saveId','')
    print('saveId : ',saveId)
    context = {'saveId':saveId}
    response = render(request,'login.html',context)
    # max_age=60초*60분*24시간*30일 (30일동안 쿠키저장(브라우저가 닫혀도)) 없을경우 브라우저 종료 시 삭제
    if not request.COOKIES.get('cookinfo'): # 쿠키 정보검색 : request.COOKIES.get('key')
      response.set_cookie('cookinfo','1111',max_age=60*60) # 쿠키 설정(저장) : response.set_cookie('key','value') <> response.delete_cookie('key','value')
    
    return response
  else:
    print('쿠키정보 : ',request.COOKIES)
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId') # checkbox(다중선택)는 원래 getlist (checkbox가 여러개 일 경우)
    print('전달 받은 정보 : ',id,pw,saveId)
    
    response = render(request,'login.html')
    ## 정보가 있는경우 아이디기억하기
    if saveId is not None: # 아이디저장하기 체크가 있을경우
      response.set_cookie('saveId',id,max_age=60*60) # saveId에 id정보 저장
    else:
      response.delete_cookie('saveId')
    return response
  
def login2(request):
  if request.method == 'GET':
    cookId = request.COOKIES.get('cookId','')
    context = {'cookId':cookId}      
    return render(request,'login2.html',context)
    
  else:
    response = render(request,'index.html')
    
    # 3개 정보
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId')
    
    if saveId is not None:
      response.set_cookie('cookId',id,max_age=60*60) # id값을 cookId에 넘겨줌
    else:
      response.delete_cookie('cookId')
      
    return response
  
## 상품구매
def product(request):
  if request.method =='GET':
    # 쿠키 읽어오기
    proId = request.COOKIES.get('proId','')
    proName = request.COOKIES.get('proName','')
    context = {'proId':proId,'proName':proName}
    return render(request,'product.html',context)
  
  else:
    response = render(request, 'index.html') # 구매버튼 누르면 메인페이지로
    
    pId = request.POST.get('pId')
    pName = request.POST.get('pName')
    pOption = request.POST.get('pOption')
    saveProduct = request.POST.get('saveProduct')
    
    if saveProduct is not None:
      # 쿠키 저장
      response.set_cookie('proId',pId,max_age=60*60)
      response.set_cookie('proName',pName,max_age=60*60)
    else:
      response.delete_cookie('proId')
      response.delete_cookie('proName')
    
    return response
  
def m2(request):
  if request.method=='GET':
    # 쿠키 읽어오기
    mId = request.COOKIES.get('mId','')
    mMoney = request.COOKIES.get('mMoney','')
    mOption = request.COOKIES.get('mOption','')
    context = {'mId':mId,'mMoney':mMoney,'mOption':mOption}
    return render(request, 'm2.html', context)
  
  else:
    response = render(request,'index.html')
    
    memberId = request.POST.get('memberId')
    money = request.POST.get('money')
    option = request.POST.get('option')
    saveMember = request.POST.get('saveMember')
    
    if saveMember is not None:
      response.set_cookie('mId',memberId,max_age=60*60)
      response.set_cookie('mMoney',money,max_age=60*60)
      response.set_cookie('mOption',option,max_age=60*60)
    else:
      response.delete_cookie('mId')
      response.delete_cookie('mMoney')
      response.delete_cookie('mOption')
    
    return response