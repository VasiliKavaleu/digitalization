from django.urls import path
from . import views


app_name = 'set'

urlpatterns = [
    path('set_detail/', views.set_detail, name='set_detail'),
    path('change_set/<int:degree_id>/', views.change_set, name='change_set'),
    path('remove_indicator/<int:degree_id>/', views.remove_indicator, name='remove_indicator'),
    ]