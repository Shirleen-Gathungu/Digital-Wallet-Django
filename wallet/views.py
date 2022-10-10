from locale import currency
from django.shortcuts import render,redirect
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
from .forms import AccountRegistrationForm
from .models import Account
from .models import Customer
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
       form = CurrencyRegistrationForm(request.POST)
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

def register_account(request):
   if request.method=="POST":
       form =AccountRegistrationForm(request.POST)
       if form.is_valid():
           form.save()
   else:
       form = AccountRegistrationForm()
  
   return render(request,"wallet/register_account.html",
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
 rewards = Reward.objects.all()
 return render(request,'wallet/reward_list.html',
    {"Reward":rewards}
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
 loan = Loan.objects.all()
 return render(request,'wallet/loan_list.html',
    {"Loan":loan}
   )
 
def list_receipt(request):
 receipt= Receipt.objects.all()
 return render(request,'wallet/receipt_list.html',
    {"Receipt":receipt}
   )

 
def list_account(request):
 account= Account.objects.all()
 return render(request,'wallet/account_list.html',
    {"Account":account}
   )

def customer_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,'wallet/customer_profile.html',
        {"customer":customer}
    )

def edit_customer(request,id):
    edit=Customer.objects.get(id=id)
    if request.method=="POST":
        form = CustomerRegistrationForm(request.POST,instance=edit)
        if form.is_valid():
           form.save()
        return redirect("customer_profile",id=edit.id)

    else:
        form = CustomerRegistrationForm(instance=edit)
    return render(request,"wallet/edit_customer.html",
    {"form":form})


def wallet_profile(request,id):
    wallet = Wallet.objects.get(id=id)
    return render(request,'wallet/wallet_profile.html',
        {"wallet":wallet}
    )

def edit_wallet(request,id):
    wallet=Wallet.objects.get(id=id)
    if request.method=="POST":
        form = WalletRegistrationForm(request.POST,instance=wallet)
        if form.is_valid():
           form.save()
        return redirect("wallet_profile",id =wallet.id)

    else:
        form = WalletRegistrationForm(instance=wallet)
    return render(request,"wallet/edit_wallet.html",
    {"form":form})


def account_profile(request,id):
    account = Account.objects.get(id=id)
    return render(request,'wallet/account_profile.html',
        {"account":account}
    )



def edit_account(request,id):
    accounts=Account.objects.get(id=id)
    if request.method=="POST":
        form = AccountRegistrationForm(request.POST,instance=accounts)
        if form.is_valid():
           form.save()
        return redirect("account_profile",id =accounts.id)

    else:
        form = AccountRegistrationForm(instance=accounts)
    return render(request,"wallet/edit_account.html",
    {"form":form})


def card_profile(request,id):
    card = Card.objects.get(id=id)
    return render(request,'wallet/card_profile.html',
        {"card":card}
    )



def edit_card(request,id):
    card=Card.objects.get(id=id)
    if request.method=="POST":
        form = CardRegistrationForm(request.POST,instance=card)
        if form.is_valid():
           form.save()
        return redirect("card_profile",id =card.id)

    else:
        form = CardRegistrationForm(instance=card)
    return render(request,"wallet/edit_card.html",
    {"form":form})





def receipt_profile(request,id):
    receipt = Receipt.objects.get(id=id)
    return render(request,'wallet/receipt_profile.html',
        {"receipt":receipt}
    )


def edit_receipt(request,id):
    receipts=Receipt.objects.get(id=id)
    if request.method=="POST":
        form = ReceiptRegistrationForm(request.POST,instance=receipts)
        if form.is_valid():
           form.save()
        return redirect("receipt_profile",id=receipts.id)

    else:
        form = ReceiptRegistrationForm(instance=receipts)
    return render(request,"wallet/edit_receipt.html",
    {"form":form})



def transaction_profile(request,id):
    transaction = Transaction.objects.get(id=id)
    return render(request,'wallet/transaction_profile.html',
        {"transaction":transaction}
    )

def edit_transaction(request,id):
    transactions=Transaction.objects.get(id=id)
    if request.method=="POST":
        form = TransactionRegistrationForm(request.POST,instance=transactions)
        if form.is_valid():
           form.save()
        return redirect("transaction_profile",id=transactions.id)

    else:
        form = TransactionRegistrationForm(instance=transactions)
    return render(request,"wallet/edit_transaction.html",
    {"form":form})

