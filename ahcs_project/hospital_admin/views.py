from django.shortcuts import render

# Create your views here.
def hospital_admin_dashboard(request):
    context={ }
    return render(request,"hospital_admin/hospital_admin_dashboard.html",context)
