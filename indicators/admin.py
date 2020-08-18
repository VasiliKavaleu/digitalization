from django.contrib import admin
from .models import Degree, AnswerChoice


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ['name', 'business_process']


@admin.register(AnswerChoice)
class AnswerChoiceAdmin(admin.ModelAdmin):
    list_display = ['answer']



