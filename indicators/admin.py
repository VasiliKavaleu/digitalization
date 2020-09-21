from django.contrib import admin

from .models import Degree, AnswerChoice, AnswerInput


class AnswerChoiceInline(admin.TabularInline):
    model = AnswerChoice


class AnswerInputInline(admin.TabularInline):
    model = AnswerInput


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [AnswerChoiceInline, AnswerInputInline]


@admin.register(AnswerChoice)
class AnswerChoiceAdmin(admin.ModelAdmin):
    list_display = ['answer']
    list_filter = ('question',)


@admin.register(AnswerInput)
class AnswerInputAdmin(admin.ModelAdmin):
    list_filter = ('question',)

