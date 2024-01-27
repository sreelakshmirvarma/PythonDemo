from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect


from django.shortcuts import render
from django.urls import reverse




from .models import Departments
from .models import Doctors

from .forms import BookingForm

# Create your views here.
def index(request):

    return render(request, "index.html")
def About(request):
    return render(request, "about.html")
def Booking(request):
    if request.method == "POST":
        form =BookingForm(request.POST)
        
        if form.is_valid():
            form.save()
    form= BookingForm()
    dict_form={
            'form': form
        }
    return render(request, "booking.html", dict_form)

def Save(request):
    if request.method == "POST":
        form =BookingForm(request.POST)
        
        if form.is_valid():
         form.save()
    form= BookingForm()
    return HttpResponseRedirect(reverse('booking'))

            
            

def Doctorss(request):
    dict_docs={
        'doctors': Doctors.objects.all()
        }
    return render(request, "doctors.html", dict_docs)
   
def Contact(request):
    return render(request, "contact.html")
def Department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request, "department.html", dict_dept)


