from django.shortcuts import render
from .models import Customer

def account_info(request):
    customer = Customer.objects.all()
    return render(request, 'customer_accounts/account_info.html', {'customer': customer})

def home(request):
    return render(request, 'customer_accounts/home.html')