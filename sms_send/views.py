from django.shortcuts import render, redirect
from django.http import HttpResponse
from twilio.rest import Client
from sms_send.models import SMS
from django.contrib.auth.decorators import login_required
from usersapp.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


#from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

@login_required
def home(request):
    context ={
        'smss': SMS.objects.filter(author=request.user)
        }
    return render(request, 'home.html', context)

def register(request):
	if request.method == 'POST' :
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()		
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request,user)	
			messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')					
			return redirect('home')
	else :
		form = UserRegistrationForm()
	return render(request,'registration/register.html',{'form' : form})



def sms_bank(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        message = request.POST['message']
        
        account_sid = 'AC779da2d9977ed154c5ec91ef134fcb55'
        auth_token = '55658f6e7a7ed16d5c6ed01293712d10'
        client = Client(account_sid, auth_token)
        
        try:
            message = client.messages.create(
                body=message,
                messaging_service_sid='MGafff0df1a25ea000bd3bae816198bc94',
                to=recipient
                
            )
            return HttpResponse('SMS envoyé avec succès')
        except Exception as e:
            return HttpResponse(f'Erreur lors de l\'envoi du SMS : {str(e)}')
    return render(request, 'sms_bank.html')

def sms_kms(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        message = request.POST['message']
        
        account_sid = 'AC779da2d9977ed154c5ec91ef134fcb55'
        auth_token = '55658f6e7a7ed16d5c6ed01293712d10'
        client = Client(account_sid, auth_token)
        
        try:
            message = client.messages.create(
                body=message,
                messaging_service_sid='MGe9d576c5963b974abff497aed21d2909',
                to=recipient
                
            )
            return HttpResponse('SMS envoyé avec succès')
        except Exception as e:
            return HttpResponse(f'Erreur lors de l\'envoi du SMS : {str(e)}')
    return render(request, 'sms_kms.html')