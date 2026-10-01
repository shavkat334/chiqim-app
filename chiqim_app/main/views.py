from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
def home_view(request):
    return render(request, 'dashboard.html')



def profile(request):
    return render(request, 'profile.html')

def categories(request):
    return render(request, 'categories.html')

def expenses_form(request):
    return render(request, 'expense_form.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("main:home_sahifa")
    
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        consent = request.POST.get("consent_status") == "on"  

   
        if password != password2:
            messages.error(request, "")
            return redirect("main:register_sahifa")

    
        if User.objects.filter(username=email).exists():
            messages.error(request, "Siz bu emaildan allaqachon ro'yxatdan o'tgansiz!")
            return redirect("main:register_sahifa")

        
        new_user = User.objects.create_user(
            first_name=name,
            last_name=last_name,
            username=email,  
            email=email,     
            password=password
        )

       
        Profile.objects.create(
            consent = True if consent == "on" else False,
            user=new_user 
        )

        messages.success(request, "Siz muvaffaqqiyatli ro'yxatdan o'tdingiz!")
        return redirect("main:login_sahifa")

    return render(request, 'register.html')


def expenses(request):
    return render(request, 'expenses.html')
