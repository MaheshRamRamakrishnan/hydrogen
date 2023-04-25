from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('monitering_home/', views.moniter_home),
    path('monitering_login/', views.moniter_login),
    path('monit_register/', views.m_register)

]
