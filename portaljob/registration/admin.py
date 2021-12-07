from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class UserEmployee(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('name_enterprise',
                        'nif_stat','is_recruiter','is_trainer'
            )}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name_enterprise','nif_stat','is_recruiter','is_trainer')}),
    )    
    
# Register your models here.
admin.site.register(User,UserEmployee)
