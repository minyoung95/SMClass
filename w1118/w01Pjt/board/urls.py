from django.urls import path,include
from . import views

app_name = 'board'
urlpatterns = [
    path('board/',views.board,name='board')
]
