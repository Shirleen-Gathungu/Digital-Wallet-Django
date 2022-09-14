from locale import currency
from django.shortcuts import render
from .forms import CustomerRegistrationForm
from .forms import CardRegistrationForm
from .forms import WalletRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import RewardRegistrationForm
from .forms import CurrencyRegistrationForm
from .forms import ThirdPartyRegistrationForm
from .forms import LoanRegistrationForm
from .forms import ReceiptRegistrationForm
from .models import Customer, Notification, ThirdParty
from .models import Card
from .models import Wallet
from .models import Transaction
from .models import Notification
from .models import Reward
from .models import Currency
from .models import ThirdParty
from .models import Loan
from .models import Receipt
# Create your views here.
def register_customer(request):
    if request.method=="POST":
        form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",
    {"form":form})


def register_card(request):
    if request.method=="POST":
        form = CardRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = CardRegistrationForm()
    return render(request,"wallet/register_card.html",
    {"form":form})

def register_wallet(request):
    if request.method=="POST":
        form = WalletRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",
    {"form":form})

def register_transaction(request):
    if request.method=="POST":
        form =TransactionRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = TransactionRegistrationForm()
   
    return render(request,"wallet/register_transaction.html",
    {"form":form})

def register_notification(request):
    if request.method=="POST":
        form =NotificationRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",
    {"form":form})

def register_reward(request):

    if request.method=="POST":
        form =RewardRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = RewardRegistrationForm()
    
    return render(request,"wallet/register_reward.html",
    {"form":form})

def register_currency(request):
    if request.method=="POST":
        form =CurrencyRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = CurrencyRegistrationForm()
    
    
    return render(request,"wallet/register_currency.html",
    {"form":form})

def register_thirdparty(request):

    if request.method=="POST":
        form =ThirdPartyRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = ThirdPartyRegistrationForm()
    
    return render(request,"wallet/register_thirdparty.html",
    {"form":form})


def register_loan(request):
    if request.method=="POST":
        form =LoanRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = LoanRegistrationForm()
   
    return render(request,"wallet/register_loan.html",
    {"form":form})

def register_receipt(request):
    if request.method=="POST":
        form =ReceiptRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = ReceiptRegistrationForm()
    
    return render(request,"wallet/register_receipt.html",
    {"form":form})


def list_customers(request):
    customers=Customer.objects.all()
    return render(request,'wallet/customer_list.html',
    {"Customer":customers})


def list_card(request):
    cards=Card.objects.all()
    return render(request,'wallet/card_list.html',
     {"Card":cards}
    )

def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request,'wallet/wallet_list.html',
     {"Wallet":wallets}
    )

def list_transaction(request):
    transactions=Transaction.objects.all()
    return render(request,'wallet/transaction_list.html',
     {"Transaction":transactions}
    )


def list_notifications(request):
  notifications=Notification.objects.all()
  return render(request,'wallet/notification_list.html',
     {"Notification":notifications}
    )


def list_rewards(request):
  rewards=Reward.objects.all()
  return render(request,'wallet/reward_list.html',
     {"Rewards":rewards}
    )

def list_currency(request):
  currency=Currency.objects.all()
  return render(request,'wallet/currency_list.html',
     {"Currency":currency}
    )

def list_thirdparty(request):
  thirdparty=ThirdParty.objects.all()
  return render(request,'wallet/thirdparty_list.html',
     {"ThirdParty":thirdparty}
    )

def list_loan(request):
  loan=Loan.objects.all()
  return render(request,'wallet/loan_list.html',
     {"Loan":loan}
    )

def list_receipt(request):
  receipt= Receipt.objects.all()
  return render(request,'wallet/receipt_list.html',
     {"Receipt":receipt}
    )
