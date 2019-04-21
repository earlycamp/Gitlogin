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

@login_required
def land(request):

 	# from github api
	orgUser=[k['login'] for k in __import__('requests').get(config('api_url_base').strip()).json()]
	conf = config('List')
	logedUser = str(request.user)

	if logedUser in conf or orgUser:
		verifiedUser = logedUser


	return render(request, 'land.html', locals())

@login_required
def lesson(request):
    return render(request, 'lesson.html')

@login_required
def login2(request):
    return render(request, 'login2.html')

@login_required
def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')

@login_required
def login(request):
    return render(request, 'login.html')
 

def kickout(request):
    return render(request, 'kickout.html')

@login_required
def main (request):
    return render(request, 'main.html')

@login_required
def week2(request):
    return render(request, 'week2.html')

@login_required
def week3(request):
    return render(request, 'week3.html')

@login_required
def week4(request):
    return render(request, 'week4.html')

@login_required
def week5(request):
    return render(request, 'week5.html')

@login_required
def week6(request):
    return render(request, 'week6.html')

@login_required
def week7(request):
    return render(request, 'week7.html')

@login_required
def week8(request):
    return render(request, 'week8.html')

@login_required
def week9(request):
    return render(request, 'week9.html')

@login_required
def week10(request):
    return render(request, 'week10.html')

@login_required
def week11(request):
    return render(request, 'week11.html')
