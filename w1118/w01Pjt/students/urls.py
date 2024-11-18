from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
    path('write/',views.write, name='write1'), # 학생입력페이지
    path('list/',views.list, name='list'), # 학생리스트
    path('<str:name>/view/',views.view, name='view'), # 학생상세페이지 // 정수일 경우 <int:no(변수명)>
    
    path('<str:name>/modify/',views.modify, name='modify'), # url 수정 <str:name> : 매개변수
    path('modify2/',views.modify2,name='modify2'), # 파리미터 수정 (매개변수 x)
    path('<str:name>/modify3/',views.modify3, name='modify3'), # appname 수정
    
    path('<str:name>/delete/',views.delete, name='delete'), # 학생정보삭제
]
