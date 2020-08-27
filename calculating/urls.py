from django.urls import path
from . import views


app_name = 'calculating'

urlpatterns = [
    path('questionnaire/<int:indicator_id>/', views.questionnaire, name='questionnaire'),
    path('questionnaire/<int:indicator_id>/calculate_value/', views.calculate_value_from_answer, name='calculate_value_from_answer'),
    path('/get_result/', views.get_result_of_value, name='get_result_of_value'),
    ]
