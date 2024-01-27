from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.About, name='about'),
    path('booking/', views.Booking, name='booking'),
    path('save/', views.Booking, name='save'),
    path('doctors/', views.Doctorss, name='doctors'),
    path('contact/', views.Contact, name='contact'),
    path('department/', views.Department, name='department'),
 
]