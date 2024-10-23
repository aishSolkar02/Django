from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def login(request):
    return render(request,"login.html")

#=========================Register Page ==========================

def register(request):
    if request.method=="GET":
        form=UserCreationForm()
        return render(request,"register.html",{"form":form})
    else:
        submited_form=UserCreationForm(request.POST)
        if submited_form.is_valid():
            submited_form.save()
            return HttpResponseRedirect("/login")


