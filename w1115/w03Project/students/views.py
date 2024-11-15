from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student
# Create your views here.
def write(request):
  return render(request,'stu_write.html')

## 학생정보 저장
def save(request):
  if request.POST:
    print('학생정보 저장')
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print(name,major,grade,age,gender)
    qs = Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
    qs.save()
  return HttpResponseRedirect(reverse('index'))

def list(request):
  qs = Student.objects.all()
  context = {'list':qs}
  
  return render(request,'stu_list.html',context)