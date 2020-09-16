from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

from .paginator_helper import pg_records
from set.set import Set
from .models import Degree
from .forms import ContactForm


def main(request):
    return render(request, 'main.html')

def choose_indicator(request):
    """Reflecting selected indicators."""
    if request.user.is_authenticated:
        indicators = Degree.objects.all()
        set = Set(request)
        list_id_in_set = [int(i) for i in request.session.get(settings.SET_SESSION_ID).keys()]
        context = pg_records(request, indicators, 5)
        context['list_id_in_set'] = list_id_in_set
        return render(request, 'indicators.html', context)
    return redirect('account:login_user')

def contact_us(request):
    """Sending email."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            organisation = form.cleaned_data['organisation']
            email = form.cleaned_data['email']
            message_in = form.cleaned_data['message']

            recipients = ['WASILIY10K@yandex.ru']
            subject = 'Портал цифровизации'
            message_out = name + '\n' + email + '\n' + organisation + '\n' + '\n' + message_in

            try:
                send_mail(subject, message_out, settings.EMAIL_HOST_USER, recipients)
            except BadHeaderError:
                return redirect('contact_us')
            else:
                messages.success(request, 'Сообщение успешно отправлено!')
                return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
