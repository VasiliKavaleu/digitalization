from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from indicators.models import Degree


def calculate_value_of_indicator(request, indicator_id):
    """Calculate value of indicator in accordance with options (multiple choice or not)"""
    indicator = get_object_or_404(Degree, id=indicator_id)
    business_process = request.POST['business_process']
    interim_set = request.session.get(settings.SET_SESSION_ID)
    answer_options = indicator.answerchoice_set.all()

    if indicator.multiple_answer:
        multiple_values_of_selected_choices = (request.POST.getlist('choice'))
        if not multiple_values_of_selected_choices:
            raise KeyError
        sum_of_values_of_selected_choices = sum(list((map(int, multiple_values_of_selected_choices))))
        sum_of_the_values_of_all_possible_options = sum([option.value for option in answer_options])
        value_of_indicator = sum_of_values_of_selected_choices / sum_of_the_values_of_all_possible_options
    else:
        value_of_selected_choice = int(request.POST['choice'])
        max_value_of_answer_options = max([option.value for option in answer_options])
        value_of_indicator = value_of_selected_choice / max_value_of_answer_options
    save_value_of_indicator_to_set(request, interim_set, indicator_id, value_of_indicator, business_process)


def save_value_of_indicator_to_set(request, interim_set, indicator_id, value_of_indicator, business_process):
    """Save calculated date to current sessions."""
    interim_set[str(indicator_id)]['value'] = str(value_of_indicator)
    interim_set[str(indicator_id)]['business_process'] = business_process
    request.session.save()