from django.shortcuts import render,redirect
from students.models import Student

# Create your views here.

## 학생 정보입력
def write(request):
  if request.method == "POST":
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    
    # 정보 저장
    Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby)
    
    return redirect('/students/list/') ## 리스트로 이동 (redirect?)
  
  else:
    return render(request,'write.html')

## 학생 전체리스트
def list(request):
  qs = Student.objects.all()
  context = {'slist':qs}
  return render(request,'list.html',context)

## 상세 정보
def view(request,name): # name도 받음
  qs = Student.objects.get(name=name) # name으로 정보를 찾음
  context = {'stu':qs}
  return render(request,'view.html',context)

## 학생정보수정, 수정저장
def update(request,name): 
  if request.method == 'GET': # 수정버튼을 누르면 그 학생의 정보를 input창에
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request,'update.html',context) # update창에 띄워줌
  
  else: # 수정 저장버튼을 누를때
    name = request.POST.get('name')
    name = request.POST.get('name')
    name = request.POST.get('name')
    name = request.POST.get('name')
    name = request.POST.get('name')
    name = request.POST.get('name')