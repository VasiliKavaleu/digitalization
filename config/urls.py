from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('indicators.urls')),
    path('account', include('account.urls', namespace='account')),
    path('set/', include('set.urls', namespace='set')),
    path('calculating/', include('calculating.urls', namespace='calculating')),
]
