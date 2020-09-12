from django import forms


TYPE_OF_BUSINESS_PROCESS = [
    (None, '---'),
    ('Управления', 'Управления'),
    ('Основные', 'Основные'),
    ('Вспомогательные', 'Вспомогательные'),
]

class ChooseBusinessProcessForm(forms.Form):
    business_process = forms.ChoiceField(
                                        label="Бизнес-процесс:",
                                         widget=forms.Select(attrs={"class": "form-control"}),
                                         choices=TYPE_OF_BUSINESS_PROCESS
                                         )


class InputValueForm(forms.Form):
	quantity = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"}))
	total_quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={"class": "form-control"}))

