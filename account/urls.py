from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [

	path('register', views.register, name="register"),
	path('login_user', views.login_user, name="login_user"),
	path('logout_user', views.logout_user, name="logout_user"),
	path('update_user', views.update_user, name="update_user"),
	path('del_user', views.del_user, name="del_user"),

]