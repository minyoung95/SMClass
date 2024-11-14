from django.shortcuts import render

# Create your views here.
def eve(request):
    return render(request, 'everegister.html')