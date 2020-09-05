from django import forms


class ChooseDegreeForm(forms.Form):
	copy = forms.BooleanField(required=False, label='Выбрать')


class ContactForm(forms.Form):
	name = forms.CharField(max_length=100, label='Имя', widget=forms.TextInput(
		attrs={'class': 'form-control'}
	))

	organisation = forms.CharField(max_length=254, label='Организация', widget=forms.TextInput(
		attrs={'class': 'form-control'}
	))

	email = forms.EmailField(max_length=254, label='Email', help_text='Это поле обязательно', widget=forms.EmailInput(
		attrs={'class': 'form-control'}
	))

	message = forms.CharField(label='Сообщение', widget=forms.Textarea(
		attrs={'class': 'form-control'}
	))

