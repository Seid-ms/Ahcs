from django.shortcuts import render

# Create your views here.
def physician_dashboard(request):
    context={ }
    return render(request,"physician/physician_dashboard.html",context)

def view_waiting_list(request):
    context={ }
    return render(request,"physician/forms/view_waiting_list.html",context)
def add_prescription(request):
    context={ }
    return render(request,"physician/forms/prescription_form.html",context)
def add_xray_request(request):
    context={ }
    return render(request,"physician/forms/xray_form.html",context)