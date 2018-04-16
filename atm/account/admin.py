from django.contrib import admin
from .models import up
from django.contrib.auth.models import User
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
# 	list_display=['username','password']
# admin.site.register(User,UserAdmin)

class upAdmin(admin.ModelAdmin):
	list_display=['user','yuan_balance','dollar_balance','hk_balance','annuity']
admin.site.register(up,upAdmin)
