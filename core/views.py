from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    if request.user.is_authenticated:
        return redirect("account:account")
    return render(request, "core/index.html")

def contact(request):
    return render(request, "core/contact.html")

def about(request):
    return render(request, "about-us.html")

def career(request):
    return render(request, 'career.html')


