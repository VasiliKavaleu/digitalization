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
        if calculated_result['digitalization_of_manage_bp'][1]  or calculated_result['digitalization_of_manage_bp'][1] == 0:
            self.result['digitalization_of_manage_bp'] = calculated_result['digitalization_of_manage_bp'][1]
        if calculated_result['digitalization_of_main_bp'][1]  or calculated_result['digitalization_of_main_bp'][1] == 0:
            self.result['digitalization_of_main_bp'] = calculated_result['digitalization_of_main_bp'][1]
        if calculated_result['digitalization_of_auxiliary_bp'][1] or calculated_result['digitalization_of_auxiliary_bp'][1] == 0:
            self.result['digitalization_of_auxiliary_bp'] = calculated_result['digitalization_of_auxiliary_bp'][1]



        self.save()

    def save(self):
        self.session.modified = True