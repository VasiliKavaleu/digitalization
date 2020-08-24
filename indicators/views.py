from django.shortcuts import render, redirect
from django.conf import settings

from set.set import Set
from .models import Degree


def main(request):
    print(request.session.get(settings.SET_SESSION_ID))
    return render(request, 'main.html')

def choose_indicator(request):
    """Reflecting selected indicators."""
    if request.user.is_authenticated:
        indicators = Degree.objects.all()
        set = Set(request)
        list_id_in_set = [int(i) for i in request.session.get(settings.SET_SESSION_ID).keys()]
        return render(request, 'indicators.html', {'indicators': indicators, 'list_id_in_set': list_id_in_set})
    return redirect('account:login_user')

def contact_us(request):
    return render(request, 'contact.html')



