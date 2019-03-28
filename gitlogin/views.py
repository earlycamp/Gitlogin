from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def land(request):

	c = "Blackadams" , "gitkata" , "Frank Tamre" , "Victor M" , "Peter Muturi" , "Kipsmthn"
	d = str(request.user)

	return render(request, 'land.html', locals())

def sorry(request):
    return render(request, 'sorry.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

