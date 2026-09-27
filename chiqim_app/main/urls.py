from django.urls import path, include
from .views import *
app_name = 'main'

urlpatterns = [
    path('', home_view, name="home_sahifa"),
    path('profile/', profile, name="profile_sahifa"),
    path('categories/', categories, name="categoriya_sahifa"),
    path('expense_form/', expenses_form, name="expenses_form"),
    path('login/', login, name="login_sahifa"),
    path('register/', register, name="register_sahifa"),
    path('expenses/', expenses, name="expenses_sahifa")

]
