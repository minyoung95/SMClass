from django.urls import path,include
from . import views

app_name = ''
urlpatterns = [
    path('',views.home,name='home.html')
]
