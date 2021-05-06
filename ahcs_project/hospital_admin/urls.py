from django.urls import path
from . import views

urlpatterns = [
     path('hospital_admin_dashboard/',views.hospital_admin_dashboard,name='hospital_admin_dashboard'),
]