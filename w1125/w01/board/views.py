from django.shortcuts import render,redirect
from board.models import Board
from member.models import Member
from django.db.models import F
from datetime import datetime

# Create your views here.
def blist(request):
  qs = Board.objects.all().order_by('-bgroup','bstep')
  context = {'blist':qs}
  return render(request,'blist.html',context)

def bwrite(request):
  if request.method == 'GET':
    return render(request,'bwrite.html')
  else:
    # id = request.POST.get('id')
    id = request.session.get('session_id')
    member = Member.objects.get(id=id) # id로 찾은 member데이터 저장
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bfile = request.FILES.get('bfile','') # 없을 땐 공백
    print('파일이름 : ',request.FILES)
    print('파일이름2 : ',bfile)
    
    # DB 저장 - AutoField : 번호생성
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno # 같은번호
    qs.save()
    
    context = {'wmsg':'1'}
    return render(request,'bwrite.html',context)

def bview(request,bno):
  # 쿠키사용기간 - 1일동안 유지 (하루 지나면 조회수 증가 가능)
  tomorrow = datetime.replace(datetime.now(),hour=23,minute=59,second=0)
  # 쿠키설정포맷 - strftime: 시간
  expires = datetime.strftime(tomorrow,'%a,%d-%b-%Y %H:%M:%S GMT')
    
  # 조회수 증가 get()
  # qs = Board.objects.get(bno=bno)
  # qs.bhit += 1
  # qs.save()
  # context = {'board':qs}
  
  # filter() - update()

  qs = Board.objects.filter(bno=bno)
  # ## 이전글
  # prev_qs = Board.objects.filter().order_by('-bgroup','bstep').first()
  # ## 다음글
  # next_qs = Board.objects.filter().order_by('bgroup','bstep').first()
  context = {'board':qs[0]}
  print('cookie_name : ', request.COOKIES.get('cookie_name'))
  response = render(request,'bview.html',context)  
  # 조회수가 1증가하면, cookie_name에 증가한 게시글번호를 추가 (처음 조회했을때 증가)
  if request.COOKIES.get('cookie_name') is not None: # 쿠키가 있는지 체크
    cookies = request.COOKIES.get('cookie_name')
    cookies_list = cookies.split('|')
    if str(bno) not in cookies_list:
      print('cookie_name은 있는데 번호가 안올라있으면')
      # 게시글번호 1|3|4 > 2 : 1|3|4|2
      response.set_cookie('cookie_name',cookies+f'|{bno}',expires=expires) # 번호가 존재하지 않을 시 번호 추가
      qs.update(bhit = F('bhit') + 1) # qs에서 bhit 값을 가져와서 +1 
      
  else: # 처음으로 게시글을 조회했을 때
    print('cookie_name 없으면')
    response.set_cookie('cookie_name',bno,expires=expires)
    # F함수 : 필드 값을 가져옴(참조)
    qs.update(bhit = F('bhit') + 1) # qs에서 bhit 값을 가져와서 +1
    
  return response

def bdelete(request,bno):
  qs = Board.objects.get(bno=bno)
  qs.delete()
  context = {'dmsg':bno}
  return render(request,'blist.html',context)

def bupdate(request,bno):
  if request.method == "GET":
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'bupdate.html',context)
  else:
    bno = request.POST.get('bno')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    qs = Board.objects.get(bno=bno)
    qs.btitle=btitle
    qs.bcontent=bcontent
    qs.save()
    return redirect('board:bview',bno)
  
def breply(request,bno):
  if request.method == "GET":
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'breply.html',context)
  else:
    id = request.POST.get('id')
    member = Member.objects.get(id=id)
    bgroup = int(request.POST.get('bgroup')) # 답글 묶음
    bstep = int(request.POST.get('bstep')) # 답글 순서
    bindent = int(request.POST.get('bindent')) # 들여쓰기
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    
    ## 같은 bgroup에 속한 bstep이 더 큰 것만 검색 후 데이터 1씩 증가
    qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep) #__gt : 현재보다 큰
    qs.update(bstep = F('bstep')+1)
    
    qs = Board(member=member,btitle=btitle,bcontent=bcontent,bgroup=bgroup,bstep=bstep+1,\
      bindent=bindent+1)
    qs.save()
    
    context = {'rmsg':'1'}
    return render(request,'breply.html',context)