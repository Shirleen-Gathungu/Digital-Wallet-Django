from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from wallet.models import Customer
from wallet.models import Wallet
from wallet.models import Account
from wallet.models import Card
from wallet.models import Transaction
from wallet.models import Loan
from wallet.models import Receipt
from wallet.models import Notification

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields=("first_name","age","address","gender")
    

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields= ('balance','customer','date_created','status','currency','history','pin')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields= ('account_name','account_number','account_type','account_balance','wallet')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields= ('card_number','card_type','expiry_date','security_code','date_of_issue','wallet','account','issuer')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=('message','wallet','transaction_amount','transaction_charge','transaction_type','origin_account','destination_account')


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan
        fields=('loan_id','loan_type','loan_balance','amount','guaranter','issuer','wallet')


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Receipt
        fields=('receipt_type','date','receipt_number','amount','transaction','receipt_file')

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=('message','date','recipient','title')

