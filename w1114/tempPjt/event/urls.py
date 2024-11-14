from django.urls import path,include
from . import views # . : 현재폴더

app_name = 'eve' # 앱이름으로 찾아 들어올수 있게
urlpatterns = [
    # url 주소, views.py 함수명, url이름
    # http://127.0.0.1:8000/students/reg/
    # students:reg
    path('eve/',views.eve,name='eve')
]