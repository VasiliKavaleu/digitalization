from django.urls import path

from . import views


urlpatterns = [
	path('', views.main, name="main"),
	path('choose_indicator', views.choose_indicator, name="choose_indicator"),
	path('contact_us', views.contact_us, name="contact_us"),
	path('total_info', views.total_info, name="total_info"),
	path('formation_indicators', views.formation_indicators, name="formation_indicators"),
	path('methods', views.methods, name="methods"),

]