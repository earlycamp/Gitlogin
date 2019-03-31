"""gitproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from gitlogin import views 
from django.conf.urls import url, include


urlpatterns = [



    # path('students/', include(([
    #     # path('', views.student, name='student'),
    #     path('login', views.students, name='students'),
    #     path('land', views.land, name='land'),
    # ], 'classroom'), namespace='students')),
    

    # path('staff/', include(([
    #     path('login', views.staff, name='staff'),
    # ], 'classroom'), namespace='staff')),


    #  path('admins/', include(([
    #     path('login', views.staff, name='staff'),
    # ], 'classroom'), namespace='admins')),


    
    path('land/', views.land, name='land'),
    path('sorry/', views.sorry, name='sorry'),
    path('', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout2'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='login.html'), name = 'logout'),


]
