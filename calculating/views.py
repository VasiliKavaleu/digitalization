from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse

from indicators.models import Degree
from .forms import ChooseBusinessProcessForm
from .services import calculate_value_of_indicator


def questionnaire(request, indicator_id):
    form = ChooseBusinessProcessForm()
    indicator = get_object_or_404(Degree, id=indicator_id)
    return render(request, 'questionnaire.html', {'indicator': indicator, 'form': form})


def calculate_value_from_answer(request, indicator_id):
    """Calculating value of indicator"""
    print(request.session.get(settings.SET_SESSION_ID))
    form = ChooseBusinessProcessForm()
    interim_set = request.session.get(settings.SET_SESSION_ID)
    indicator = get_object_or_404(Degree, id=indicator_id)
    try:
        calculate_value_of_indicator(request, indicator_id)
    except KeyError:
        return render(request, 'questionnaire.html',
                      {'indicator': indicator, 'error_message': "Выберите вариант ответа!", 'form': form})
    return render(request, 'set_detail.html', {'interim_set': interim_set})






