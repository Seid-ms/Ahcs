from django.shortcuts import render

# Create your views here.
def lab_technician_dashboard(request):
    context={}
    return render(request,"lab_technician/lab_technician_dashboard.html",context)
    

