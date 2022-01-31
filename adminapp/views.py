from django.shortcuts import render, redirect

# Create your views here.
def admin_login(request):
    if request.method == "POST":
        name = request.POST.get('email')
        password = request.POST.get('password')

        if name =='admin' and password =='admin':
            return redirect('admin-home')
        elif name =='fazal' and password =='fazal':
            return redirect('admin-home')
        else:
            print('Invalid Login')
        
    return render(request,'main/admin-login.html')

def admin_home(request):
    return render(request,'admin/adminhome.html')    


def admin_addproduct(request):
    return render(request,'admin/addproduct.html')
def admin_viewproduct(request):
    return render(request,'admin/viewproducts.html')
def admin_viewuser(request):
    return render(request,'admin/view users.html')
def admin_feedback(request):
    return render(request,'admin/feedback.html')
