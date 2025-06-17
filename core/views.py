from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count
from .models import Transaction
from userauths.models import User

def index(request):
    if request.user.is_authenticated:
        return redirect("account:account")
    return render(request, "core/index.html")

def under_construction(request):
    return render(request, "core/under_construction.html")

def help_center(request):
    return render(request, "core/help_center.html")

def faq(request):
    return render(request, "core/faq.html")

def contact(request):
    return render(request, "core/contact.html")

def about(request):
    # Get total number of completed transactions
    total_transactions = Transaction.objects.count()
    # Get total number of users
    total_users = User.objects.count()
    
    context = {
        "total_transactions": total_transactions,
        "total_users": total_users
    }
    return render(request, "about-us.html", context)

def career(request):
    return render(request, 'career.html')

def features(request):
    return render(request, 'features.html')


