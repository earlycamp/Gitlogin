import os
from django.shortcuts import render
from decouple import config
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView



class MarkDown(TemplateView):
    template_name = 'lesson.html'

    def get_context_data(self, **kwargs):
        markdowntext = open('gitlogin/templates/hello.md').read()

        context = super(MarkDown, self).get_context_data(**kwargs)
        context['markdowntext'] = markdowntext

        return context


def land(request):

 	# from github api
	orgUser=[k['login'] for k in __import__('requests').get(config('api_url_base').strip()).json()]
	conf = config('List')
	logedUser = str(request.user)

	if logedUser in conf or orgUser:
		verifiedUser = logedUser


	return render(request, 'land.html', locals())


def lesson(request):
    return render(request, 'lesson.html')


def login2(request):
    return render(request, 'login2.html')


def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')
def login(request):
    return render(request, 'login.html')
    
def kickout(request):
    return render(request, 'kickout.html')

def main (request):
    return render(request, 'main.html')

def week2(request):
    return render(request, 'week2.html')

def week3(request):
    return render(request, 'week3.html')

def week4(request):
    return render(request, 'week4.html')

def week5(request):
    return render(request, 'week5.html')

def week6(request):
    return render(request, 'week6.html')

def week7(request):
    return render(request, 'week7.html')

def week8(request):
    return render(request, 'week8.html')

def week9(request):
    return render(request, 'week9.html')

def week10(request):
    return render(request, 'week10.html')

def week11(request):
    return render(request, 'week11.html')
