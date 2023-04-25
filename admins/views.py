from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError

def ad_home(request):
    return render(request, 'admin/admin_home.html')

def ad_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if email == "admin@gmail.com" and password == "admin" or "ADMIN":
            print(email)
            request.session['admin'] = "admin@gmail.com"
            messages.info(request, "Admin login successfully")
            return render(request, 'admin/admin_home.html')
        elif email != "admin@gmail.com":
            messages.error(request, "Wrong Mail id")
            return render(request, 'admin/admin_l.html')
        elif password != "admin":
            messages.error(request, "wrong password")
            return render(request, 'admin/admin_l.html')
        else:
            return render(request, 'admin/admin_l.html')
    return render(request, 'admin/admin_l.html')