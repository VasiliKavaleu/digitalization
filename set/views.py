from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from indicators.models import Degree
from .set import Set
from django.conf import settings


@login_required
def set_detail(request):
    """Reflecting content of set."""
    interim_set = request.session.get(settings.SET_SESSION_ID)
    print(f'Выбранные показатели {interim_set}')
    if not interim_set:
        messages.error(request, 'Выберите показатель!')
        return redirect('choose_indicator')
    return render(request, 'set_detail.html', {'interim_set': interim_set})


def add_indicator(request, indicator_id):
    """Adding indicator into set."""
    set = Set(request)
    indicator = get_object_or_404(Degree, id=indicator_id)
    set.add_to_set(indicator=indicator)
    return redirect('choose_indicator')


def remove_indicator(request, indicator_id):
    """Del indicator from set."""
    set = Set(request)
    indicator = get_object_or_404(Degree, id=indicator_id)
    set.remove_from_set(indicator=indicator)
    return redirect('choose_indicator')


def change_indicator_state(request):
    if request.is_ajax and request.method == "GET":
        indicator_id =request.GET.get("indicator_id", None)
        interim_set = request.session.get(settings.SET_SESSION_ID)
        if indicator_id in interim_set:
            remove_indicator(request, indicator_id)
        else:
            add_indicator(request, indicator_id)
        return JsonResponse({"change_state":True}, status=200)
    return JsonResponse({}, status=400)
