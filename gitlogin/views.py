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


def login(request):
    return render(request, 'login.html')


def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')

