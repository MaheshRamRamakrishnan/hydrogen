from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from management.models import *


# Create your views here.
def manage_1_home(request):
    return render(request, 'management/manage_home.html')


def management_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        city = request.POST['city']
        password = request.POST['password']
        try:
            management_registration(name=name, email=email, password=password, phonenumber=phonenumber,
                                    city=city).save()
            return redirect('/management_register/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/management_register/')
    return render(request, 'management/manage_l.html')


def management_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            r = management_registration.objects.get(email=email, password=password)
            request.session['user'] = email
            messages.info(request, 'Your login successfully! and session started')
            return redirect('/management_home1/')
        except:
            pass
    return render(request, 'management/manage_l.html')
