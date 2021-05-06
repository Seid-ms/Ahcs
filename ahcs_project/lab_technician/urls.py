from django.urls import path
from . import views

urlpatterns = [
    path('lab_technician_dashboard/',views.lab_technician_dashboard,name='lab_technician_dashboard'),
]
