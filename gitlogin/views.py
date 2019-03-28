from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def land(request):

	c = "Blackadams" , "gitkata" , "Frank Tamre" , "Victor M" , "Peter Muturi" , "Kipsmthn"
	d = str(request.user)

	return render(request, 'land.html', locals())

   

























def students(request):
    return render(request, 'students.html')

def student(request):
    return render(request, 'student.html')

def staff(request):
    return render(request, 'staff.html')

def admins(request):
    return render(request, 'admins.html')


def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

