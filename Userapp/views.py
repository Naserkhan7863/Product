import email
from unicodedata import name
from django.forms import PasswordInput
from django.shortcuts import redirect, render

from Userapp.models import UserRegisterModel
def home(request):
    return render(request,'main/index.html')
# Create your views here.
def home1(request):
    return render(request,'main/mobile.html')
def home2(request):
    return render(request,'main/laptop.html')

def home3(request):
    return render(request,'main/smarttv.html')

def home4(request):
    return render(request,'main/smartwatch.html')

def home5(request):
    return render(request,'main/contact.html')
def home6(request):
    return render(request,'main/viewcart.html')


def home7(request):

    if request.method == "POST":
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        UserRegisterModel.objects.create(email=email,contact=contact,password=password)
    return render(request,'main/Registration.html')


def home8(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            check=UserRegisterModel.objects.get(email=email,password=password)
            request.session["user_id"]=check.user_id
            return redirect("home6")
        except:
            pass
    return render(request,'main/user-login.html')
#Admin Login

