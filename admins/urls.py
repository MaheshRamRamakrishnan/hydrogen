from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('admi_home/', views.ad_home),
    path('admin_login/', views.ad_login)

]
