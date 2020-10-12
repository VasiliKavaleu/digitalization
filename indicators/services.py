from django.conf import settings

from .paginator_helper import pg_records
from set.set import Set
from account.models import Industry


def get_context(request, indicators):
    industry = Industry.objects.all()
    set = Set(request)
    list_id_in_set = [int(i) for i in request.session.get(settings.SET_SESSION_ID).keys()]
    context = pg_records(request, indicators, 5)
    context['list_id_in_set'] = list_id_in_set
    context['industries'] = industry
    return context