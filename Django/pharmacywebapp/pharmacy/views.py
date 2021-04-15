from django.shortcuts import render, HttpResponse
from datetime import datetime
from pharmacy.models import AddUser
from pharmacy.models import AddMedicine
from django.contrib import messages
# Create your views here.
def index(request):
    #return HttpResponse("this is home page")
    return render(request, 'index.html')

#def adminlogin(request):
    #return HttpResponse("this is admin login page")

def staticpages(request):
    #return HttpResponse("this is a static page, nothing is being performed here for now")
    return render(request,'loginaboutcontact.html')

def addUser(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        bloodgroup = request.POST.get('bloodgroup')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        adduser= AddUser(name=name, age=age, sex=sex, bloodgroup=bloodgroup, email=email, phonenumber=phonenumber, address=address, date=datetime.today())
        adduser.save()
        messages.success(request, 'New customer added to the database!')
    return render(request,'addUser.html')

def addMedicine(request):
    if request.method == "POST":
        name = request.POST.get('name')
        batch = request.POST.get('batch')
        manufacture = request.POST.get('manufacture')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        date = request.POST.get('date')
        addmedicine= AddMedicine(name=name, batch=batch, manufacture=manufacture, quantity=quantity, price=price, date=date)
        addmedicine.save()
        messages.success(request, 'New medicine added to the database!')
    return render(request,'addMedicine.html')