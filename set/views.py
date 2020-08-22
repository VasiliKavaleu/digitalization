from django.shortcuts import render, redirect, get_object_or_404

from indicators.models import Degree
from .set import Set
from django.conf import settings


def set_detail(request):
    """Reflecting content of set."""
    interim_set = request.session.get(settings.SET_SESSION_ID)
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