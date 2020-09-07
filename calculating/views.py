from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError

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
        print(result)
        return render(request, 'result1.html', {'values': result})
    else:
        return render(request, 'set_detail.html', {'interim_set': interim_set, 'error_message': "Заполните опросные листы!"})

from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage

def save_result(request):
    result_session = request.session.get(settings.RESULT_SESSION_ID)
    if request.method == 'POST':
        agreement_to_send = request.POST['send_email']
        if agreement_to_send == 'agree':


            # html_string = render_to_string('pdf.html', {'result_session': result_session}) #first
            # response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'filename="order.pdf"'
            # weasyprint.HTML(string=html_string).write_pdf(response)
            # return response

            html_string = render_to_string('pdf.html', {'result_session': result_session})  # second
            html = weasyprint.HTML(string=html_string)
            result_pdf = html.write_pdf('test.pdf')
            recipients = ['WASILIY10K@yandex.ru']
            subject = 'Портал цифровизации'
            msg = EmailMessage(subject, subject, settings.EMAIL_HOST_USER, recipients)
            msg.attach_file('test.pdf')
            msg.send()
            return redirect('calculating:show_history_of_evaluations')


        else:
            result_session = request.session.get(settings.RESULT_SESSION_ID)
            data = UserResultDigitalization(user=request.user, digitalization=result_session['digitalization'])
            data.save()
            messages.success(request, 'Результат успешно сохранен!')
            return redirect('calculating:show_history_of_evaluations')



def show_history_of_evaluations(request):
    results_of_digitalization = UserResultDigitalization.objects.filter(user=request.user).order_by('-date_added')
    return render(request, 'saved_result.html', {'results_of_digitalization': results_of_digitalization})


def calculate_value_of_indicator_share(request, indicator_id):
    interim_set = request.session.get(settings.SET_SESSION_ID)
    if request.method == "POST":
        input_data = InputValueForm(request.POST)
        business_process = request.POST['business_process']
        if input_data.is_valid():
            quantity = input_data.cleaned_data["quantity"]
            total_quantity = input_data.cleaned_data["total_quantity"]
            if quantity <= total_quantity:
                value_of_indicator = str(quantity/total_quantity)
                save_value_of_indicator_to_set(request, interim_set, indicator_id, value_of_indicator, business_process)
                return render(request, 'set_detail.html', {'interim_set': interim_set})
            else:
                return redirect('calculating:questionnaire', indicator_id)
                # indicator = get_object_or_404(Degree, id=indicator_id)
                # input_value_form = InputValueForm()
                # return render(request, 'questionnaire.html',
                #               {"indicator": indicator, "error_message": "Проверьте введенные значения!", "input_value_form": input_value_form})







