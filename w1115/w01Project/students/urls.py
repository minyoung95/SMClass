from django.urls import path,include
from . import views

app_name = 'students' # app이름 : 이름으로 접근할 때 사용
urlpatterns = [
    path('write/', views.write, name='write'), # 함수이름
    path('save/', views.save, name='save'), 
    path('list/', views.list, name='list'), 
]
