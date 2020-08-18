from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
        #Leave as empty string for base url
	path('register', views.register, name="register"),
	path('login_user', views.login_user, name="login_user"),
	path('logout_user', views.logout_user, name="logout_user"),


]