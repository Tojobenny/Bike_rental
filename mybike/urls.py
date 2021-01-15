"""mybike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from mysite import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('bike/',views.bike,name='bike'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('team/',views.team,name='index'),
    path('blog_home/',views.blog_home,name='blog_home'),
    path('blog_single/',views.blog_single,name='blog_single'),
    path('elements/',views.elements,name='elements'),
    path('newuser/',views.newuser,name='newuser'),
    path('loggin/',views.loggin,name='login'),
    path('admins/',views.admins,name='admins'),
    path('booking/<str:regno>/',views.booking,name='booking'),
    path('logout/',views.logout,name='logout'),
    path('paymen/',views.paymen,name='paymen')


]
