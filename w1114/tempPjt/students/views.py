from django.shortcuts import render

# Create your views here.
def regStudent(request): # 요청
    return render(request,'register.html') # render() : 페이지열기