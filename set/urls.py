from django.urls import path
from . import views


app_name = 'set'

urlpatterns = [
    path('set_detail/', views.set_detail, name='set_detail'),
    path('add_indicator/<int:indicator_id>/', views.add_indicator, name='add_indicator'),
    path('remove_indicator/<int:indicator_id>/', views.remove_indicator, name='remove_from_set'),

    path('change_indicator_state/', views.change_indicator_state, name='change_indicator_state'),


    ]