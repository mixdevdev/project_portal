from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class UserEmployee(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name_enterprise',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name_enterprise',)}),
    )    
    
# Register your models here.
admin.site.register(User,UserEmployee)
