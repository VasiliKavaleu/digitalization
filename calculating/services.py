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


def calculate_values_of_digitalization(request):
    interim_set = request.session.get(settings.SET_SESSION_ID)
    main_bp_values = []
    manage_bp_values = []
    auxiliary_bp_values = []

    for indicator in interim_set.values():
        if indicator['business_process'] == 'Основные':
            main_bp_values.append(indicator['value'])
        elif indicator['business_process'] == 'Вспомогательные':
            auxiliary_bp_values.append(indicator['value'])
        elif indicator['business_process'] == 'Управления':
            auxiliary_bp_values.append(indicator['value'])
        else:
            return None

    digitalization_of_main_bp = calculate_rms_value(main_bp_values)
    digitalization_of_manage_bp = calculate_rms_value(manage_bp_values)
    digitalization_of_auxiliary_bp = calculate_rms_value(auxiliary_bp_values)

    total_digitalization = calculate_rms_value([i for i in [
                                                            digitalization_of_main_bp,
                                                            digitalization_of_manage_bp,
                                                            digitalization_of_auxiliary_bp
                                                            ] if i is not None])
    return {
        'digitalization_of_manage_bp': ['Цифровизация бизнес процессов управления', transf_to_int_percent(digitalization_of_manage_bp)],
        'digitalization_of_main_bp': ['Цифровизация основных бизнес процессов', transf_to_int_percent(digitalization_of_main_bp)],
        'digitalization_of_auxiliary_bp': ['Цифровизация вспомогательных бизнес процессов', transf_to_int_percent(digitalization_of_auxiliary_bp)],
        'total_digitalization': ['Цифровизация', transf_to_int_percent(total_digitalization)]
            }
    # return {
    #     'digitalization_of_manage_bp': digitalization_of_manage_bp,
    #     'digitalization_of_main_bp': digitalization_of_main_bp,
    #     'digitalization_of_auxiliary_bp': digitalization_of_auxiliary_bp,
    #     'total_digitalization': total_digitalization
    #         }


def calculate_rms_value(arr):
    a = sum(list(map(lambda x: float(x) ** 2, arr)))
    b = len(arr)
    try:
        result = (a / b) ** 0.5
    except ZeroDivisionError:
        return None
    else:
        return result

def transf_to_int_percent(value):
    if value:
        return int(round(value, 2)*100)
    return value