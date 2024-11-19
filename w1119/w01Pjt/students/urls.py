from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
    path('write/',views.write,name='write'),
    path('search/',views.search,name='search'),
    path('list/',views.list,name='list'),
    path('view/<str:name>/',views.view,name='view'), ## name 넘기기
    path('update/<str:name>/',views.update,name='update'), ## name 넘기기
    # path('update/',views.update,name='update'), ## name 넘기기
    path('delete/<str:name>/',views.delete,name='delete'),
]
