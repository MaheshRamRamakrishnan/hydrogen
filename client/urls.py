from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('client_home/', views.c_home),
    path('client_register/', views.c_register),
    path('client_login/', views.client_login)

]
