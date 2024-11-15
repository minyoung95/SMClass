from django.urls import path,include
from . import views

app_name = '' # app이름 : 이름으로 접근할 때 사용
urlpatterns = [
    path('', views.index, name='index') # 함수이름
]
