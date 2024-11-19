from django.shortcuts import render,redirect
from students.models import Student
from django.urls import reverse

# Create your views here.

## 학생입력페이지(GET), 학생저장(POST)
def write(request):
  if request.method == "POST":
    name = request.POST.get('name') # 데이터 없을때 None
    major = request.POST['major'] # 데이터 없을때 error
    grade = request.POST['grade'] 
    age = request.POST['age']
    gender = request.POST['gender']
    # hobby = request.POST['hobby'] # 취미 여러개 고르기 불가(1개만 넘어옴)
    hobbys = request.POST.getlist('hobby') # checkbox 데이터 여러개 가져오기
    # hobby = ','.join(hobbys) # list -> str 타입으로 변경
    # hobby_list = hobby.split(',') # str -> list 타입으로 변경
   
    ## qs.save()
    # qs = Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)
    # qs.save()
    
    ## create : save() 필요없음
    Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)
    
    return redirect('/students/list/')
  else: # GET 호출
    # templates 폴더에서 html 파일 검색
    return render(request,'write.html')
  
## 학생검색
def search(request):
  search = request.GET.get('search')
  print('검색단어 search : ',search)
  ## 데이터 검색부분
  qs = Student.objects.filter(name=search) # (name__contains__=search) : 홍 검색하면 홍 자 포함된 이름 다 검색
  context = {'slist':qs}
  return render(request,'list.html',context)

## 전체학생 리스트
def list(request):
  ## 전체 학생정보 가져오기
  # qs = Student.objects.all()
  qs = Student.objects.order_by('grade','name').all() # 학년 순으로 정렬 후 이름 순(역순은 변수에 -)
  context = {'slist':qs} 
  return render(request,'list.html',context)

## 학생 상제정보
def view(request,name):
  qs = Student.objects.get(name=name)
  context = {'stu':qs}
  return render(request,'view.html',context)

## 학생 정보수정, 수정저장
def update(request,name):
  if request.method == "GET": # 수정버튼 누를때
    # name = request.GET['name']
    print(name)
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request,'update.html',context)
  else: # 수정페이지에서 저장버튼을 누를때
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    
    # Student 검색
    qs = Student.objects.get(name=name)
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.hobby = hobby
    qs.save()
    
    return redirect('students:view',name)
    # return redirect(reverse('students:view',args=(name,))) # args의 데이터를 students의 view로 보냄
    
## 학생정보 삭제
def delete(request,name):
  print('삭제정보 이름 : ',name)
  Student.objects.get(name=name).delete() # name으로 검색하여 삭제
  return redirect('/students/list')