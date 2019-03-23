from django.shortcuts import render

# Create your views here.

def land(request):
    return render(request, 'land.html')


def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

