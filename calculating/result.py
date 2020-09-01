from django.conf import settings


class ResultSession(object):
    def __init__(self, request):
        """Initialization result."""
        self.session = request.session
        result = self.session.get(settings.RESULT_SESSION_ID)
        if not result:
            result = self.session[settings.RESULT_SESSION_ID] = {}
        self.result = result

    def save_to_result_session(self, calculated_result):
        """Adding values into result session."""
        self.result['digitalization'] = calculated_result['total_digitalization'][1]
        self.save()

    def save(self):
        self.session.modified = True