from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sms_send.urls')),
    path('', include('usersapp.urls')),
]