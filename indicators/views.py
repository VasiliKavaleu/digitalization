from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Degree
from .forms import ContactForm
from .services import get_context


def main(request):
    return render(request, 'main.html')

@login_required
def choose_indicator(request):
    """Reflecting selected indicators."""
    if not request.GET.getlist('Industry[]'):
        indicators = Degree.objects.all()
        return render(request, 'indicators.html', get_context(request, indicators))
    else:
        indicators = Degree.objects.filter(industry__in=request.GET.getlist('Industry[]'))
        return render(request, 'indicators.html', get_context(request, indicators))


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


def total_info(request):
    return render(request, 'description/total_info.html')


def methods(request):
    return render(request, 'description/methods.html')


def formation_indicators(request):
    return render(request, 'description/formation_indicators.html')

