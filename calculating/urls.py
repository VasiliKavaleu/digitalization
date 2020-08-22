from django.urls import path
from . import views


app_name = 'calculating'

urlpatterns = [
    path('questionnaire/<int:indicator_id>/', views.questionnaire, name='questionnaire'),
    ]