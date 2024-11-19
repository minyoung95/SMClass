from django.contrib import admin
from students.models import Student

# Register your models here.
# StudentAdmin 추가 (이름,학과,학년만 보이는)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['name','major','grade']

# admin사이트에 Student와 StudentAdmin 추가
admin.site.register(Student,StudentAdmin) 