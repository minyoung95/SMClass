from django.shortcuts import render,redirect

# Create your views here.
def write(request):
  return render(request,'write.html')