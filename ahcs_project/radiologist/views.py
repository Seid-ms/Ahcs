from django.shortcuts import render

# Create your views here.
def radiologist_dashboard(request):
    context={ }
    return render(request,"radiologist/radiologist_dashboard.html",context)
