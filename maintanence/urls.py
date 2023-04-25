from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('maintainhome/', views.maintain_home),
    path('mainregister/', views.maintenence_register),
    path('maintainlogin/', views.maintanence_login),

]
