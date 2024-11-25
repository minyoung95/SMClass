from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('member/',include('member.urls')),
    path('board/',include('board.urls')),
]


## 이미지 등록 url 추가 (MEDIA_URL로 들어오면 MEDIA_ROOT에서 파일을 찾기)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)