from django.contrib import admin
from students.models import Student
# Register your models here.

 # admin페이지에서 Student의 정보를 추가적으로 보여줌 
class StudentAdmin(admin.ModelAdmin):
  list_display =['name','major','age']

admin.site.register(Student,StudentAdmin)