from django import forms


TYPE_OF_BUSINESS_PROCESS = [
    (None, '---'),
    ('Управления', 'Управления'),
    ('Основные', 'Основные'),
    ('Вспомогательные', 'Вспомогательные'),
]

class ChooseBusinessProcessForm(forms.Form):
    business_process = forms.ChoiceField(label="Бизнес-процес", widget=forms.Select, choices=TYPE_OF_BUSINESS_PROCESS)
