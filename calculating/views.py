from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
import weasyprint
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from account.models import UserResultDigitalization
from .result import ResultSession
from indicators.models import Degree
from .forms import ChooseBusinessProcessForm, InputValueForm
from .services import calculate_value_of_indicator, calculate_values_of_digitalization, save_value_of_indicator_to_set, save_to_db


@login_required
def questionnaire(request, indicator_id):
    """Return data for question list."""
    input_value_form = InputValueForm()
    form = ChooseBusinessProcessForm()
    indicator = get_object_or_404(Degree, id=indicator_id)
    return render(request, 'questionnaire.html', {
                                                    'indicator': indicator,
                                                    'form': form,
                                                    'input_value_form': input_value_form
                                                })


@login_required
def calculate_value_of_indicator_degree(request, indicator_id):
    """Calculating value of indicator (type degree)."""
    form = ChooseBusinessProcessForm()
    interim_set = request.session.get(settings.SET_SESSION_ID)
    indicator = get_object_or_404(Degree, id=indicator_id)
    try:
        calculate_value_of_indicator(request, indicator_id)
    except KeyError:
        return render(request, 'questionnaire.html',    {
                                                        'indicator': indicator,
                                                        'error_message': "Выберите вариант ответа!",
                                                        'form': form
                                                        })
    return render(request, 'set_detail.html', {'interim_set': interim_set})


@login_required
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


@login_required
def save_result(request):
    """Saving values of digitalization into DB."""
    save_to_db(request)
    messages.success(request, 'Результат успешно сохранен!')
    return redirect('calculating:show_history_of_evaluations')


@login_required
def show_history_of_evaluations(request):
    results_of_digitalization = UserResultDigitalization.objects.filter(user=request.user).order_by('-date_added')
    return render(request, 'saved_result.html', {'results_of_digitalization': results_of_digitalization})


@login_required
def calculate_value_of_indicator_share(request, indicator_id):
    interim_set = request.session.get(settings.SET_SESSION_ID)
    if request.method == "POST":
        input_data = InputValueForm(request.POST)
        business_process = request.POST['business_process']
        if input_data.is_valid():
            quantity = input_data.cleaned_data["quantity"]
            total_quantity = input_data.cleaned_data["total_quantity"]
            if quantity <= total_quantity:
                value_of_indicator = str(round(quantity/total_quantity, 2))
                save_value_of_indicator_to_set(request, interim_set, indicator_id, value_of_indicator, business_process)
                return render(request, 'set_detail.html', {'interim_set': interim_set})
            else:
                messages.info(request, "Проверьте введенные значения!")
                return redirect('calculating:questionnaire', indicator_id)


@login_required
def generate_pdf(request, total_values_id):
    total_values_digitalization = get_object_or_404(UserResultDigitalization, id=total_values_id)
    organisation = request.user.organisation
    full_name = request.user.first_name + " " + request.user.last_name
    email = request.user.email
    html_string = render_to_string('pdf.html', {
                                                'total_values_digitalization': total_values_digitalization,
                                                'organisation': organisation,
                                                'full_name': full_name,
                                                'email': email
                                                })
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Digitalization.pdf"'
    weasyprint.HTML(string=html_string).write_pdf(response, stylesheets=[weasyprint.CSS(
                                                                        settings.STATIC_DIR + '/css/pdf.css')])
    return response


