from django.shortcuts import render

# Create your views here.
def receptionist_dashboard(request):
    context={}
    return render(request,"receptionist/receptionist_dashboard.html",context)
def register_new_patinet(request):
    context={}
    return render(request,"receptionist/form/registeration_form.html",context)