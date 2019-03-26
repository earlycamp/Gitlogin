from django.shortcuts import render

# Create your views here.

# def home(request):
# 	return render(request, 'home.html')


def land(request):
    return render(request, 'land.html')

def students(request):
    return render(request, 'students.html')

def staff(request):
    return render(request, 'staff.html')

def admins(request):
    return render(request, 'admins.html')


def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

