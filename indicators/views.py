from django.shortcuts import render, redirect
from .models import Degree
from . forms import ChooseDegreeForm


def main(request):
    return render(request, 'main.html')

def choose_indicator(request):
    if request.user.is_authenticated:
        indicators = Degree.objects.all()
        choose_degree_form = ChooseDegreeForm()
        return render(request, 'indicators.html', {'indicators': indicators, 'choose_degree_form': choose_degree_form })
    else:
        return redirect('account:login_user')

def contact_us(request):
    return render(request, 'contact.html')

def return_list_of_selected_indicator(request):
    return render(request, 'selected_indicator.html')

