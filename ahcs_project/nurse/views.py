from django.shortcuts import render

# Create your views here.
def nurse_dashboard(request):
    context={}
    return render(request,"nurse/nurse_dashboard.html",context)
def add_vital_sign(request):
    context={}
    return render(request,"nurse/form/vital_sign_form.html",context)