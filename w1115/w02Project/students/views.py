from django.shortcuts import render

# Create your views here.
def write(request):
  print('학생등록페이지 호출')
  return render(request,'stu_write.html')