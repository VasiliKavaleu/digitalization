from django.shortcuts import render, redirect
from .models import Degree
from set.set import Set
from django.conf import settings


def main(request):
    return render(request, 'main.html')

def choose_indicator(request):
    if request.user.is_authenticated:
        indicators = Degree.objects.all()
        set = Set(request)
        set_id = [int(i) for i in request.session.get(settings.SET_SESSION_ID).keys()]
        return render(request, 'indicators.html', {'indicators': indicators, 'set':set, 'set_id':set_id})
    else:
        return redirect('account:login_user')

def contact_us(request):
    return render(request, 'contact.html')

def return_list_of_selected_indicator(request):
    return render(request, 'selected_indicator.html')

