from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from client.models import *


# Create your views here.
def c_home(request):
    return render(request, 'client/client_home.html')


def c_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        city = request.POST['city']
        password = request.POST['password']
        try:
            client1_registration(name=name, email=email, password=password, phonenumber=phonenumber,
                                 city=city).save()
            return redirect('/client_register/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/client_register/')
    return render(request, 'client/client_l.html')


def client_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            r = client1_registration.objects.get(email=email, password=password)
            if r.report == True:
                request.session['user'] = email
                messages.info(request, 'Your login successfully! and session started')
                return redirect('/client_home/')
            else:
                messages.info(request, 'Your can not login! Need Management approval!!!')
        except:
            pass
    return render(request, 'client/client_l.html')
