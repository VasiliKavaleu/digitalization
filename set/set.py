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

    def add_to_set(self, indicator):
        """Adding indicator into set."""
        indicator_id = str(indicator.id)
        if indicator_id not in self.set:
            indicator_obj = Degree.objects.filter(id=indicator_id).values()
            self.set[indicator_id] = {'value': '0', 'business_process': '', 'name': indicator_obj[0]['name'], 'id': indicator_id}
        self.save()

    def remove_from_set(self, indicator):
        """Removing indicator from set."""
        indicator_id = str(indicator.id)
        if indicator_id in self.set:
            del self.set[indicator_id]
        self.save()

    def save(self):
        self.session.modified = True



    def __iter__(self): # not used
        """Iteration through degrees in the Set."""
        degree_ids = self.set.keys()
        degrees = Degree.objects.filter(id__in=degree_ids)
        for degree in degrees:
            yield degree

    def clear(self):
        """Cleaning set."""
        del self.session[settings.SET_SESSION_ID]
        self.save()

