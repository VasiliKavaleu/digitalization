from django.shortcuts import render, redirect
from django.conf import settings

from .models import Degree


def main(request):
    return render(request, 'main.html')

def choose_indicator(request):
    """Reflecting selected indicators."""
    if request.user.is_authenticated:
        indicators = Degree.objects.all()
        set_of_id = [int(i) for i in request.session.get(settings.SET_SESSION_ID).keys()]
        return render(request, 'indicators.html', {'indicators': indicators, 'set_of_id': set_of_id})
    else:
        return redirect('account:login_user')

def contact_us(request):
    return render(request, 'contact.html')



