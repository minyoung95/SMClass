from django.contrib import admin
from member.models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ['id']
  # list_display = ['id', 'pw', 'name', 'nicname']
  

admin.site.register(Member,MemberAdmin)