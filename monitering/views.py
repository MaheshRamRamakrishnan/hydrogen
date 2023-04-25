from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from monitering.models import *


# Create your views here.
def moniter_home(request):
    return render(request, 'monitering/m_home.html')


def m_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        city = request.POST['city']
        password = request.POST['password']
        try:
            moniter1_registration(name=name, email=email, password=password, phonenumber=phonenumber,
                                  city=city).save()
            return redirect('/monit_register/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/monit_register/')
    return render(request, 'monitering/moniter_l.html')


def moniter_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            r = moniter1_registration.objects.get(email=email, password=password)
            request.session['user'] = email
            messages.info(request, 'Your login successfully! and session started')
            return redirect('/monitering_home/')
        except:
            pass
    return render(request, 'monitering/moniter_l.html')
