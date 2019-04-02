from django.shortcuts import render
from decouple import config
from django.contrib.auth.decorators import login_required



def land(request):

 	# from github api
	orgUser=[k['login'] for k in __import__('requests').get(config('api_url_base').split()).json()]	
	conf = config('List')
	logedUser = str(request.user)

	if logedUser in conf or orgUser:
		verifiedUser = logedUser


	return render(request, 'land.html', locals())


def sorry(request):
    return render(request, 'sorry.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')

