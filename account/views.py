from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .models import NewUser


# Create your views here.

def register_view(request) :
    if request.method == "POST" :
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        land_owner = request.POST.get("is_land_owner")
        furniture_delivery = request.POST.get("is_furniture_delivery")
        is_land_owner = False
        if land_owner == 'true' :
            is_land_owner = True
        
        is_furniture_delivery = False
        if furniture_delivery == 'true':
            is_furniture_delivery = True
        
        
        
        if first_name and last_name and email and password :
            is_exist = NewUser.objects.filter(email = email)
            if not is_exist :
                user_obj = NewUser.objects.create_user(email= email, first_name = first_name, last_name = last_name, is_land_owner=is_land_owner,is_furniture_delivery=is_furniture_delivery, password = password)
                return render(request, 'register_page/user_created.html')
            else :
                return render(request, 'register_page/user_exist.html')
    return render(request,'register_page/register.html')


def login_view(request) :
    if request.method == "POST" :
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is None :
            context = {"error" : "Invalid user email or password."}
            return render(request, 'login_page/login.html', context)
        else :
            login(request, user)
            return redirect("/dashboard")
    return render(request, 'login_page/login.html')

def logout_view(request) :
    if request.method == "POST":
        logout(request)
        return redirect("/account/login/")
    return render(request, "logout_page/logout.html", {})

def index(request):
    return render(request, "index.html")