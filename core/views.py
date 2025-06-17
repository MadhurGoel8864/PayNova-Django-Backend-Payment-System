from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count
from .models import Transaction
from userauths.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DepositForm
from .models import Account, Notification

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

@login_required
def deposit_money(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            description = form.cleaned_data['description'] or 'Deposit'
            
            # Get user's account
            account = Account.objects.get(user=request.user)
            
            # Update account balance
            account.account_balance += amount
            account.save()
            
            # Create transaction record
            Transaction.objects.create(
                user=request.user,
                amount=amount,
                description=description,
                transaction_type='deposit',
                status='completed',
                sender=request.user,
                reciever=request.user
            )
            
            # Create notification
            Notification.objects.create(
                user=request.user,
                amount=amount,
                notification_type='Credit Alert'
            )
            
            messages.success(request, f'Successfully deposited ₹{amount} to your account.')
            return redirect('account:dashboard')
    else:
        form = DepositForm()
    
    context = {
        'form': form
    }
    return render(request, 'account/deposit.html', context)

@login_required
def deposit_history(request):
    deposits = Transaction.objects.filter(
        user=request.user,
        transaction_type='deposit'
    ).order_by('-date')
    
    context = {
        'deposits': deposits
    }
    return render(request, 'account/deposit-history.html', context)

@login_required
def transactions(request):
    sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="transfer").order_by("-id")
    reciever_transaction = Transaction.objects.filter(reciever=request.user, transaction_type="transfer").order_by("-id")
    request_sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="request")
    request_reciever_transaction = Transaction.objects.filter(reciever=request.user, transaction_type="request")
    deposits = Transaction.objects.filter(user=request.user, transaction_type="deposit").order_by("-id")

    context = {
        "sender_transaction":sender_transaction,
        "reciever_transaction":reciever_transaction,
        "request_sender_transaction":request_sender_transaction,
        "request_reciever_transaction":request_reciever_transaction,
        "deposits":deposits,
    }
    return render(request, "transaction/transaction-list.html", context)


