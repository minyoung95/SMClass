from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import Max, F
from django.contrib import messages

# Create your views here.
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {'blist':qs}
  return render(request,'blist.html',context)

def bwrite(request):
  if request.method == 'GET':
    return render(request,'bwrite.html')
  else:
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    # no = Board.objects.aggregate(max_bno = Max('bno'))
    # no['max_bno']+1
    # 오라클 sequence.nextval, sequence.currval 이 없기때문에 번호를 위 방식으로 생성
    
    ## DB저장
    # bno,bstep,bindent,bhit,bdate - 자동
    # id,btitle,bcontent - 입력
    # bgroup - 차후 입력
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno # currval = nextval
    qs.save()
    messages.success(request,message='게시글이 저장되었습니다.') # 1회
    # return redirect('board:blist')
    return render(request,'bwrite.html',{'w_msg':'1'})
  
def bview(request,bno):
  print('게시글 번호 : ',bno)
  
  ## 조회 수 1 증가 - get : save로 저장
  # qs = Board.objects.get(bno=bno)
  # qs.bhit += 1
  # qs.save()
  # context = {'board':qs} # qs
  
  ## filter : update() 여러개 동시에 할때
  qs = Board.objects.filter(bno=bno)
  qs.update(bhit = F('bhit')+1) # F함수 : 값을 가져와서 컬럼에 저장
  context = {'board':qs[0]} # qs면 에러
  return render(request,'bview.html',context)

def bmodify(request,bno):
  print('게시글 번호 : ',bno)
  if request.method == 'GET':
    qs = Board.objects.filter(bno=bno)
    context = {'board':qs[0]}
    return render(request,'bmodify.html',context)
  else:
    bno = request.POST.get('bno')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    qs.save()
    # return redirect('board:blist')
    return render(request,'bmodify.html',{'u_msg': '1'})
    
def bdelete(request,bno):
  print('게시글 번호 : ',bno)
  Board.objects.get(bno=bno).delete()
  return render(request,'blist.html',{'d_msg':bno})

def breply(request,bno):
  if request.method == "GET":
    print('게시글 번호 : ',bno)
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'breply.html',context)
  else:
    bgroup = int(request.POST.get('bgroup'))
    bstep = int(request.POST.get('bstep'))
    bindent = int(request.POST.get('bindent')) # str타입 +1 하기위해 int로 타입변경
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    print('bgroup 번호', bgroup)
    
    qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
    qs.update(bstep = F('bstep')+1) # bstep의 모든 값에 +1 > 사이에 값이 들어감
    
    # bgroup은 부모의 bgroup을 입력
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bgroup=bgroup\
      ,bstep=bstep+1,bindent=bindent+1) # 다른 답변을 달때마다 순서 +1, 들여쓰기 +1
    
    # return redirect('board:blist')
    return render(request,'blist.html',{'r_msg':'1'})