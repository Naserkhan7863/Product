"""Product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Userapp import views
from adminapp import views as adminviews


urlpatterns = [
 path('admins/', admin.site.urls),
 path('',views.home,name='home'),
 path('Mobiles',views.home1,name='home1'),
 path('Laptop',views.home2,name='home2'),
 path('Smarttv',views.home3,name='home3'),
 path('smartwatch',views.home4,name='home4'),
 path('contact',views.home5,name='home5'),
 path('viewcart',views.home6,name='home6'),
 path('Registration',views.home7,name='home7'),
 path('User-login',views.home8,name='home8'),
 
 #admin login to admin home redirection
 path('admin-login',adminviews.admin_login,name='admin-login'),
 path('admin-home',adminviews.admin_home, name='admin-home'),

 #admin dashboard redirection
  path('admin-addproduct',adminviews.admin_addproduct, name='admin_addproduct'),
  path('admin-viewproduct',adminviews.admin_viewproduct, name='admin_viewproduct'),
  path('admin-viewuser',adminviews.admin_viewuser, name='admin_viewuser'),
  path('admin-feedback',adminviews.admin_feedback, name='admin_feedback'),


              
]
