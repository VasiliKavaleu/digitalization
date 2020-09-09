from django.contrib import admin
from .models import CustomUser, UserResultDigitalization, Depatment, IndicatorMainBP, IndicatorManageBP, IndicatorAuxiliaryBP


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

@admin.register(IndicatorMainBP)
class IndicatorMainBPAdmin(admin.ModelAdmin):
    list_filter = ['name']

@admin.register(IndicatorManageBP)
class IndicatorManageBPAdmin(admin.ModelAdmin):
    list_filter = ['name']

@admin.register(IndicatorAuxiliaryBP)
class IndicatorAuxiliaryBPAdmin(admin.ModelAdmin):
    list_filter = ['name']