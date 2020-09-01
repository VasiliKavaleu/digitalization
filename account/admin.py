from django.contrib import admin
from .models import CustomUser, UserResultDigitalization


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'organisation']
    list_filter = ['organisation']

@admin.register(UserResultDigitalization)
class UserResultDigitalizationAdmin(admin.ModelAdmin):
    list_filter = ['date_added']



