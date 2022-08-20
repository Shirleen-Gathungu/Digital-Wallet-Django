from concurrent.futures.thread import _python_exit
from django.contrib import admin
from .models import Customer
from .models import Wallet
from .models import Account
from  .models import Transaction
from  .models import Notification
from  .models import Reward
from  .models import Currency
from  .models import ThirdParty
from  .models import Loan
from  .models import Receipt
from  .models import Card

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','email','phone_number','gender','age','profile_picture',)
    search_fields = ('first_name','last_name','age','email','phone_number','gender','age','profile_picture',)
admin.site.register(Customer,CustomerAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_number','expiry_date','card_type','security_code', 'date_of_issue','issuer',Wallet,Account,)
    search_fields = ('card_number','expiry_date','card_type','card_type','security_code', 'date_of_issue','issuer',Wallet,Account,)

admin.site.register(Card,CardAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display = (Customer,Currency,'balance','date_created', 'history',  )
    search_fields = (Customer,Currency,'balance','date_created', 'history', )
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display =(Wallet,'account_number','account_type',)
    search_fields = (Wallet,'account_number','account_type',)
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_amount','transaction_charge','origin_account','destination_account',Wallet,)
    search_fields = ('transaction_amount','transaction_charge','origin_account','destination_account',Wallet,)
admin.site.register(Transaction,TransactionAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('date','message',Customer,)
    search_fields = ('date','message',Customer,)
admin.site.register(Notification,NotificationAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = (Transaction,Customer,'points',)
    search_fields = (Transaction,Customer,'points',)
admin.site.register(Reward,RewardAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('country','amount','symbol_name',)
    search_fields = ('country','amount','symbol_name',)
admin.site.register(Currency,CurrencyAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = (Account,Currency,Wallet,'issuer','transaction_amount','date_of_issue',)
    search_fields = ('transaction_amount','date_of_issue',)
admin.site.register(ThirdParty,ThirdPartyAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_type','loan_balance','guaranter',Wallet,)
    search_fields = (' loan_id ','loan_type','loan_balance',' amount','guaranter',' issuer',Wallet,)
admin.site.register(Loan,LoanAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_number','date',Transaction,)
    search_fields = ('receipt_number','date',Transaction,)
admin.site.register(Receipt,ReceiptAdmin)

# Register your models here.


