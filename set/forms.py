from django import forms
from django.forms import ModelForm
from indicators.models import AnswerChoice


from django import forms

class AnswerChoiceForm(forms.Form):
    name = forms.BooleanField(required=False)