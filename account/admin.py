from django.contrib import admin
from .models import CustomUser, UserResultDigitalization, Depatment


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'organisation']
    list_filter = ['organisation']

@admin.register(UserResultDigitalization)
class UserResultDigitalizationAdmin(admin.ModelAdmin):
    list_filter = ['date_added']

@admin.register(Depatment)
class DepatmentAdmin(admin.ModelAdmin):
    list_filter = ['name']
