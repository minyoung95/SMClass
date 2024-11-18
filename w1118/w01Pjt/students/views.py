from django.shortcuts import render, redirect
from students.models import Student

# Create your views here.
def write(request):
  if request.method == 'GET': # GET과 POST로 비교하여 
    print('GET방식으로 들어옴')
    return render(request,'write.html')
  else:
    print('POST방식으로 들어옴')
    # 학생입력저장
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print('입력데이터 : ',name,major,grade,age,gender)
    ## DB 저장
    Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender)
    print('학생데이터 저장')
  return redirect('students:list') # dm에 데이터 입력 수정 등등 하면 redirect, 페이지 호출 render // students:list - appname으로 연결
  # return redirect('/students/list') # url로 연결

## 학생 리스트
def list(request):
  qs = Student.objects.all()
  context = {'slist' : qs}
  return render(request,'list.html',context) # dm에 데이터 입력 수정 등등 하면 redirect, 페이지 호출 render // views.py 에서 context(데이터 변수)도 list.html로 넘김

## 학생상세페이지
def view(request,name):
  print('이름정보 : ',name)
  qs = Student.objects.filter(name=name) # 1개의 데이터(list), 데이터 없을경우 {}
  context = {'stu':qs[0]}
  return render(request,'view.html',context)
  # qs = Student.objects.get(name=name) 없을경우 에러
  # qs = get_object_or_404(Student,name=name) # 없을경우 구문 리턴
  
## 학생 수정페이지 - url 매개변수로 전달값 받음
def modify(request,name):
  if request.method == 'GET':
    qs = Student.objects.filter(name=name) # 데이터 1개 추출
    context = {'stu':qs[0]}
    return render(request,'update.html',context)
  else:
    print('POST 호출')
    qs = Student.objects.get(name=name)
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print('수정 modify정보 :',name,major,grade,age,gender)
    # db 저장
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.save()
    return redirect('students:list') # appname이 list

## 학생 수정페이지 - 파라미터
def modify2(request):
  name = request.GET.get('name')
  print('modify2 이름정보', name)
  qs = Student.objects.filter(name=name) # 데이터 1개 추출
  context = {'stu':qs[0]}
  return render(request,'update.html',context)

## 학생 수정페이지 - appName으로 데이터 받기
def modify3(request,name):
  print('modify3 이름정보', name)
  qs = Student.objects.filter(name=name) # 데이터 1개 추출
  context = {'stu':qs[0]}
  return render(request,'update.html',context)

## 학생정보 삭제
def delete(request,name):
  print('삭제정보 : ',name)
  qs = Student.objects.get(name=name).delete()
  return redirect('students:list')

# 학생입력저장
# def doWrite(request):
#   if request.method == 'POST':
#     name = request.POST['name']
#     major = request.POST['major']
#     grade = request.POST['grade']
#     age = request.POST['age']
#     gender = request.POST['gender']
#     print('입력데이터 : ',name,major,grade,age,gender)
#   else:
#     print('해당되는 데이터가 없습니다.')
#   return redirect('/')