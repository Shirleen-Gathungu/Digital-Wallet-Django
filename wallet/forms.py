
from pyexpat import model
from re import A
from django import forms
from .models import Customer
from .models import Reward
from .models import Card
from .models import Wallet
from .models import Notification
from .models import Transaction
from .models import Currency
from .models import ThirdParty
from .models import Loan
from .models import Receipt
from django.forms import ModelForm
 
class CustomerRegistrationForm(ModelForm):
       class Meta:
           model= Customer
           fields = ['first_name','last_name','address','email','phone_number','gender','age']
           widgets={
       'first_name' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'last_name' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'address' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
         'email' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
           'phone_number' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
 
           'gender' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
      
           'age' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
     
       }
 


class CardRegistrationForm(ModelForm):
    class Meta:
        model= Card
        fields = ['card_number','card_type','expiry_date','security_code','date_of_issue','wallet','account','issuer']
        widgets={
       'card_number' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'card_type' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'expiry_date' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
         'security_code' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
           'date_of_issue' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
 
           'wallet' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
      
           'account' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
         'issuer' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
     
       }
 



class WalletRegistrationForm(ModelForm):
    class Meta:
        model= Wallet
        fields = ['balance','customer','date_created','status','currency','history','pin']
        widgets={
       'balance' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'customer' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'date_created' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
         'status' : forms.TextInput(attrs = {
                'class': 'form-control',
         }),
         'currency' : forms.TextInput(attrs = {
                'class': 'form-control',
         }),
          'history' : forms.TextInput(attrs = {
                'class': 'form-control',
         }),
         'pin' : forms.TextInput(attrs = {
                'class': 'form-control',
         })
        }

class TransactionRegistrationForm(ModelForm):
    class Meta:
        model= Transaction
        fields =['message','wallet','transaction_amount','transaction_charge','transaction_type','origin_account','destination_account']
        widgets={
       'message' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'wallet' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'transaction_amount' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'transaction_charge' : forms.TextInput(attrs = {
                'class': 'form-control',
        }),
        'transaction_type' : forms.TextInput(attrs = {
                'class': 'form-control',
         }),
        'origin_account' : forms.TextInput(attrs = {
                'class': 'form-control',
         }),
         'destination_account' : forms.TextInput(attrs = {
                'class': 'form-control',
         })
        }

class NotificationRegistrationForm(ModelForm):
    class Meta:
        model= Notification
        fields =['message','date','recipient','title']
        widgets={
       'message' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'date' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'recipient' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
       'title' : forms.TextInput(attrs = {
                'class': 'form-control',
       })
       
        }
class RewardRegistrationForm(ModelForm):
    class Meta:
        model= Reward
        fields = ['transaction','recipient','date_of_reward','points']
        widgets={
       'transaction' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'recipient' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'date_of_reward' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
       'points' : forms.TextInput(attrs = {
                'class': 'form-control',
       })
       
        }
        


class CurrencyRegistrationForm(ModelForm):
    class Meta:
        model= Currency
        fields = ['country','symbol_name','amount']
        widgets={
       'country' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'symbol_name' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'amount' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        }


class ThirdPartyRegistrationForm(ModelForm):
    class Meta:
        model= ThirdParty
        fields = ['account','transaction_amount','currency','date_of_issue','wallet','issuer']
        widgets={
       'account' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'transaction_amount' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'currency' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'date_of_issue' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'wallet' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'issuer' : forms.TextInput(attrs = {
                'class': 'form-control',
       })
        }


class LoanRegistrationForm(ModelForm):
    class Meta:
        model= Loan
        fields = ['loan_id','loan_type','loan_balance','amount','guaranter','issuer','wallet']
        widgets={
       'loan_id' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'loan_type' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'loan_balance' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'amount' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'guaranter' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'issuer' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'wallet' : forms.TextInput(attrs = {
                'class': 'form-control',
       })
        }

class ReceiptRegistrationForm(ModelForm):
    class Meta:
        model= Receipt
        fields = ['receipt_type','date','receipt_number','amount','transaction','receipt_file']
        widgets={
       'receipt_type' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'date' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
        'receipt_number' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
       'amount' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
       'transaction' : forms.TextInput(attrs = {
                'class': 'form-control',
       }),
       'receipt_file' : forms.TextInput(attrs = {
                'class': 'form-control',
       })
        }