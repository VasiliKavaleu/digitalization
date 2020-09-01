from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings

from account.models import UserResultDigitalization
from .result import ResultSession
from indicators.models import Degree
from .forms import ChooseBusinessProcessForm, InputValueForm
from .services import calculate_value_of_indicator, calculate_values_of_digitalization, save_value_of_indicator_to_set


def questionnaire(request, indicator_id):
    input_value_form = InputValueForm()
    form = ChooseBusinessProcessForm()
    indicator = get_object_or_404(Degree, id=indicator_id)
    return render(request, 'questionnaire.html', {'indicator': indicator, 'form': form, 'input_value_form': input_value_form})


def calculate_value_of_indicator_degree(request, indicator_id):
    """Calculating value of indicator"""
    form = ChooseBusinessProcessForm()
    interim_set = request.session.get(settings.SET_SESSION_ID)
    indicator = get_object_or_404(Degree, id=indicator_id)
    try:
        calculate_value_of_indicator(request, indicator_id)
    except KeyError:
        return render(request, 'questionnaire.html',
                      {'indicator': indicator, 'error_message': "Выберите вариант ответа!", 'form': form})
    return render(request, 'set_detail.html', {'interim_set': interim_set})


def get_result_of_value(request):
    """Calculating digitalization values."""
    result = calculate_values_of_digitalization(request)
    interim_set = request.session.get(settings.SET_SESSION_ID)
    if result:
        result_session = ResultSession(request)
        result_session.save_to_result_session(result)
        return render(request, 'result1.html', {'values': result})
    else:
        return render(request, 'set_detail.html', {'interim_set': interim_set, 'error_message': "Заполните опросные листы!"})


def save_result(request):
    result_session = request.session.get(settings.RESULT_SESSION_ID)
    data = UserResultDigitalization(user=request.user, digitalization=result_session['digitalization'])
    data.save()
    # return render(request, 'result1.html')
    return redirect('calculating:show_history_of_evaluations')


def show_history_of_evaluations(request):
    results_of_digitalization = UserResultDigitalization.objects.filter(user=request.user)
    for i in results_of_digitalization:
        print(i)
    return render(request, 'saved_result.html', {'results_of_digitalization': results_of_digitalization})


def calculate_value_of_indicator_share(request, indicator_id):
    interim_set = request.session.get(settings.SET_SESSION_ID)
    if request.method == "POST":
        input_data = InputValueForm(request.POST)
        business_process = request.POST['business_process']
        if input_data.is_valid():
            quantity = input_data.cleaned_data["quantity"]
            total_quantity = input_data.cleaned_data["total_quantity"]
            if quantity < total_quantity:
                value_of_indicator = str(quantity/total_quantity)
                save_value_of_indicator_to_set(request, interim_set, indicator_id, value_of_indicator, business_process)
                return render(request, 'set_detail.html', {'interim_set': interim_set})
            else:
                return redirect('calculating:questionnaire', indicator_id)
                # indicator = get_object_or_404(Degree, id=indicator_id)
                # input_value_form = InputValueForm()
                # return render(request, 'questionnaire.html',
                #               {"indicator": indicator, "error_message": "Проверьте введенные значения!", "input_value_form": input_value_form})







