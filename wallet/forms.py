from dataclasses import field,fields
from pyexpat import model
from django import forms
from .models import Card, Currency,Wallet, Customer,Transaction,Notification,Reward,Currency,ThirdParty,Loan,Receipt
from django.forms import ModelForm

class CustomerRegistrationForm(ModelForm):
    class Meta:
        model= Customer
        fields = "__all__"

class CardRegistrationForm(ModelForm):
    class Meta:
        model= Card
        fields = "__all__"

class WalletRegistrationForm(ModelForm):
    class Meta:
        model= Wallet
        fields = "__all__"


class TransactionRegistrationForm(ModelForm):
    class Meta:
        model= Transaction
        fields = "__all__"

class NotificationRegistrationForm(ModelForm):
    class Meta:
        model= Notification
        fields = "__all__"

class RewardRegistrationForm(ModelForm):
    class Meta:
        model= Reward
        fields = "__all__"

class CurrencyRegistrationForm(ModelForm):
    class Meta:
        model= Currency
        fields = "__all__"  

class ThirdPartyRegistrationForm(ModelForm):
    class Meta:
        model= ThirdParty
        fields = "__all__"  

class LoanRegistrationForm(ModelForm):
    class Meta:
        model= Loan
        fields = "__all__"  


class ReceiptRegistrationForm(ModelForm):
    class Meta:
        model= Receipt
        fields = "__all__"  