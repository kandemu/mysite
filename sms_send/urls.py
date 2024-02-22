from django.urls import path
from sms_send import views


urlpatterns =[
    path('',views.home, name='home'),
	path('/sms_bank',views.sms_bank, name='sms_bank'),
    path('/sms_kms',views.sms_kms, name='sms_kms'),
 
]