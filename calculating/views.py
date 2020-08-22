from django.shortcuts import render, redirect, get_object_or_404

from indicators.models import Degree
from django.conf import settings


def questionnaire(request, indicator_id):
    indicator = get_object_or_404(Degree, id=indicator_id)
    interim_set = request.session.get(settings.SET_SESSION_ID)
    print(indicator)
    return render(request, 'questionnaire.html', {'indicator': indicator})
