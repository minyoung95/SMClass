from django.contrib import admin
from member.models import Member
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ['id','name','nicName','mdate']

  
# admin.site.register(Member,MemberAdmin)