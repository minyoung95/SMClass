from django.shortcuts import render,redirect

# Create your views here.
def board(request):
  return render(request,'board.html')