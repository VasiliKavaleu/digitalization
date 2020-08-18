from django.urls import path
from . import views


urlpatterns = [
        #Leave as empty string for base url
	path('', views.main, name="main"),
	path('choose_indicator', views.choose_indicator, name="choose_indicator"),
	path('contact_us', views.contact_us, name="contact_us"),
	path('selected_indicator', views.return_list_of_selected_indicator, name="selected_indicator"),

]