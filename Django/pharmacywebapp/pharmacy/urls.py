from django.contrib import admin
from django.urls import path
from pharmacy import views

urlpatterns = [
    path("", views.index, name='home'),
    #path("adminlogin", views.adminlogin, name='adminlogin'),
    path("loginaboutcontact", views.staticpages, name='loginaboutcontact'),
    path("home", views.index, name='home'),
    path("addUser", views.addUser, name='addNewUser'),
    path("addMedicine", views.addMedicine, name='addNewMedicine'),
]