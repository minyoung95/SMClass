from django.contrib import admin
from board.models import Board

# Register your models here.
@admin.register(Board)
class BoardrAdmin(admin.ModelAdmin):
  list_display = ['bno','btitle','bgroup','bdate']