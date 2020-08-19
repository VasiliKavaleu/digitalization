from decimal import Decimal
from django.conf import settings
from indicators.models import Degree


class Set(object):
    def __init__(self, request):
        """Initialization set."""
        self.session = request.session
        set = self.session.get(settings.SET_SESSION_ID)
        if not set:
            set = self.session[settings.SET_SESSION_ID] = {}
        self.set = set

    def add_or_del(self, degree):
        """Adding degree into cart and deleting quantity."""
        degree_id = str(degree.id)
        if degree_id not in self.set:
            self.set[degree_id] = {'selected': True}
        else:
            del self.set[degree_id]
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, degree):
        """Removing degrees from cart."""
        degree_id = str(degree.id)
        if degree_id in self.set:
            del self.set[degree_id]
        self.save()

    def __iter__(self):
        """Iteration through degrees in the Set."""
        degree_ids = self.set.keys()
        degrees = Degree.objects.filter(id__in=degree_ids)
        for degree in degrees:
            yield degree



    def clear(self):
        """Cleaning set."""
        del self.session[settings.SET_SESSION_ID]
        self.save()

