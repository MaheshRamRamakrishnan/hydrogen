from django.shortcuts import render


# Create your views here.


def h_home(request):
    return render(request, 'home/home1.html')


