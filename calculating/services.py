from django.conf import settings
from django.shortcuts import get_object_or_404

from indicators.models import Degree
from account.models import UserResultDigitalization


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
        value_of_indicator = round((sum_of_values_of_selected_choices / sum_of_the_values_of_all_possible_options), 2)
    else:
        value_of_selected_choice = int(request.POST['choice'])
        max_value_of_answer_options = max([option.value for option in answer_options])
        value_of_indicator = round((value_of_selected_choice / max_value_of_answer_options), 2)
    save_value_of_indicator_to_set(request, interim_set, indicator_id, value_of_indicator, business_process)


def save_value_of_indicator_to_set(request, interim_set, indicator_id, value_of_indicator, business_process):
    """Save calculated data to current sessions."""
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
            manage_bp_values.append(indicator['value'])
        else:
            # in case questionaire did not fild out
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
    """Transformation to percent format."""
    if value or value == 0:
        return int(round(value, 2)*100)
    return value


def save_to_db(request):
    """Saving calculating values of digitalization of all business processes,total value and values of indicators."""
    result_session = request.session.get(settings.RESULT_SESSION_ID)
    print(f'result_session до сохранения в бд: {result_session}')
    try:
        digitalization_of_main_bp = result_session['digitalization_of_main_bp']
    except KeyError:
        digitalization_of_main_bp = None
    try:
        digitalization_of_manage_bp = result_session['digitalization_of_manage_bp']
    except KeyError:
        digitalization_of_manage_bp = None
    try:
        digitalization_of_auxiliary_bp = result_session['digitalization_of_auxiliary_bp']
    except KeyError:
        digitalization_of_auxiliary_bp = None

    total_data_digitalization = UserResultDigitalization.objects.create(user=request.user,
                                                                        digitalization=result_session['digitalization'],
                                                                        digit_value_main_bp=digitalization_of_main_bp,
                                                                        digit_value_manage_bp=digitalization_of_manage_bp,
                                                                        digit_value_auxiliary_bp=digitalization_of_auxiliary_bp)
    interim_set = request.session.get(settings.SET_SESSION_ID)
    for indicator in interim_set.values():
        if indicator['business_process'] == 'Основные':
            total_data_digitalization.indicatormainbp_set.create(name=indicator['name'],
                                                                      value_of_indicator=indicator['value'])
        elif indicator['business_process'] == 'Вспомогательные':
            total_data_digitalization.indicatorauxiliarybp_set.create(name=indicator['name'],
                                                                      value_of_indicator=indicator['value'])
        elif indicator['business_process'] == 'Управления':
            total_data_digitalization.indicatormanagebp_set.create(name=indicator['name'],
                                                                      value_of_indicator=indicator['value'])

    print(f'interim_set before: {interim_set}')
    print(f'result_session before: {result_session}')
    result_session.clear()
    interim_set.clear()
    print(f'result_session after: {result_session}')
    print(f'interim_set after: {interim_set}')