from django.shortcuts import render, redirect, get_object_or_404
from indicators.models import Degree
from .set import Set


def change_set(request, degree_id):
    """Adding (del) degree into (from) set."""
    set = Set(request)
    degree = get_object_or_404(Degree, id=degree_id)
    set.add_or_del(degree=degree)
    return redirect('choose_indicator')

def set_detail(request):
    """Reflecting content of set."""
    set = Set(request)
    return render(request, 'set_detail.html', {'set': set})

def remove_indicator(request, degree_id):
    """Adding (del) degree into (from) set."""
    set = Set(request)
    degree = get_object_or_404(Degree, id=degree_id)
    set.remove(degree=degree)
    return redirect('set:set_detail')