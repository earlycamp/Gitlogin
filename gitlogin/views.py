from django.shortcuts import render
from decouple import config
from django.contrib.auth.decorators import login_required



def land(request):

 	# from github api
	z=[k['login'] for k in __import__('requests').get("https://api.github.com/orgs/earlycamp/members").json()]
	print(z)


	c = config('List')
	d = str(request.user)
	print(request.user)

	return render(request, 'land.html', locals())


def sorry(request):
    return render(request, 'sorry.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')

