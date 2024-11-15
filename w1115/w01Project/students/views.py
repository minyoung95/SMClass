from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student

### 학생 전체리스트 호출
def list(request):
  qs = Student.objects.all() # 전체 학생리스트 가져오기
  context = {'list':qs} # 정보전달 변수

  return render(request,'stu_list.html',context)


# 학생입력페이터 호출
def write(request):
  print('학생등록페이지 호출')
  return render(request,'stu_write.html')

# 학생입력 저장
def save(request):
  # if request.POST =='POST': # POST 방식으로 왔나 체크
  if request.POST: # 데이터가 있는지 체크
    print('학생입력 저장')
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print(name,major,grade,age,gender)
    qs = Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
    qs.save()   
  return HttpResponseRedirect(reverse('index')) # 함수이름 index로 이동
  # redirect('/') # url
  # return redirect('index') # 페이지 넘어가기
  # return redirect(reverse('index')) # reverse : app_name
  
  