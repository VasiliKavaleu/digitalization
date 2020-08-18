from django import forms


class ChooseDegreeForm(forms.Form):
	copy = forms.BooleanField(required=False, label='Выбрать')


