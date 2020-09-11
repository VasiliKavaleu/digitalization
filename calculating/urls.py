from django.urls import path
from . import views


app_name = 'calculating'

urlpatterns = [
    path('questionnaire/<int:indicator_id>/', views.questionnaire, name='questionnaire'),
    path('questionnaire/<int:indicator_id>/calculate_value/', views.calculate_value_of_indicator_degree, name='calculate_value_of_indicator_degree'),
    path('questionnaire/<int:indicator_id>/calculate_value_of_share/', views.calculate_value_of_indicator_share, name='calculate_value_of_indicator_share'),
    path('get_result/', views.get_result_of_value, name='get_result_of_value'),
    path('save_result/', views.save_result, name='save_result'),
    path('history_of_evaluations/', views.show_history_of_evaluations, name='show_history_of_evaluations'),
    path('generate_pdf/<int:total_values_id>/', views.generate_pdf, name='generate_pdf'),
    ]
