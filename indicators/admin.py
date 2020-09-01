from django.contrib import admin

from .models import Degree, AnswerChoice, AnswerInput


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(AnswerChoice)
class AnswerChoiceAdmin(admin.ModelAdmin):
    list_display = ['answer']


admin.site.register(AnswerInput)
