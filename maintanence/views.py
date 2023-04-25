from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from maintanence.models import *


# Create your views here.
def maintain_home(request):
    return render(request, 'maintanance/main_home.html')


def maintenence_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        city = request.POST['city']
        password = request.POST['password']
        try:
            maintanance_registration(name=name, email=email, password=password, phonenumber=phonenumber,
                                     city=city).save()
            return redirect('/mainregister/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/mainregister/')
    return render(request, 'maintanance/maintanance_l.html')


def maintanence_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            r = maintanance_registration.objects.get(email=email, password=password)
            request.session['user'] = email
            messages.info(request, 'Your login successfully! and session started')
            return redirect('/maintainhome/')
        except:
            pass
    return render(request, 'maintanance/maintanance_l.html')
