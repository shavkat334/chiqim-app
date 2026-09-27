from django.shortcuts import render

def home_view(request):
    return render(request, 'dashboard.html')



def profile(request):
    return render(request, 'profile.html')

def categories(request):
    return render(request, 'categories.html')

def expenses_form(request):
    return render(request, 'expense_form.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def expenses(request):
    return render(request, 'expenses.html')
