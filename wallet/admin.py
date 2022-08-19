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

# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('first_name','last_name','age','email',)
#     search_fields = ('first_name','last_name','age','email',)
admin.site.register(Customer)

# class CardAdmin(admin.ModelAdmin):
#     list_display = ('card_type','security_code', 'date_of_issue','issuer',)
#     search_fields = ('card_type','security_code', 'date_of_issue','issuer',)

admin.site.register(Card)


# class WalletAdmin(admin.ModelAdmin):
#     list_display = ('date_created',)
#     search_fields = ('date_created',)
admin.site.register(Wallet)

# class AccountAdmin(admin.ModelAdmin):
#     list_display = (' account_number','  account_type','  account_balance',)
#     search_fields = (' account_number','  account_type','  account_balance',)
admin.site.register(Account)

# class TransactionAdmin(admin.ModelAdmin):
#     list_display = ('transaction_amount',)
#     search_fields = ('message ','transaction_amount',)
admin.site.register(Transaction)

# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ('date','  title ',)
#     search_fields = ('date','  title ',)
admin.site.register(Notification)

# class RewardAdmin(admin.ModelAdmin):
#     list_display = ('date_of_reward ',)
#     search_fields = ('date_of_reward ',)
admin.site.register(Reward)

# class CurrencyAdmin(admin.ModelAdmin):
#     list_display = ('country','amount',)
#     search_fields = ('country','amount',)
admin.site.register(Currency)

# class ThirdPartyAdmin(admin.ModelAdmin):
#     list_display = ('transaction_amount','date_of_issue',)
#     search_fields = ('transaction_amount','date_of_issue',)
admin.site.register(ThirdParty)

# class LoanAdmin(admin.ModelAdmin):
#     list_display = ('loan_type',' amount','guaranter',' issuer',)
#     search_fields = ('loan_type',' amount','guaranter',' issuer',)
# admin.site.register(Loan)

# class ReceiptAdmin(admin.ModelAdmin):
#     list_display = (' receipt_type','date','receipt_number','   amount',' receipt_file ',)
#     search_fields = (' receipt_type','date','receipt_number','   amount',' receipt_file ',)
admin.site.register(Receipt)

# Register your models here.


# class WalletAdmin(admin.ModelAdmin):
#     list_display = ('balance','customer', 'amount','date_created','status','currency','history','pin',)
#     search_fields = ('balance','customer', 'amount','date_created','status','currency','history','pin',)
# admin.site.register(Wallet,WalletAdmin)

# class AccountAdmin(admin.ModelAdmin):
#     list_display = ('account_name', 'account_number','account_type','account_balance','wallet',)
#     search_fields = ('account_name','account_number','wallet',)
# admin.site.register(Account,AccountAdmin)

# class TransactionAdmin(admin.ModelAdmin):
#     list_display = ('message', 'wallet','transaction_description','transaction_amount','transaction_charge','transaction_type','receipt','account')
#     search_fields = ('message', 'wallet','transaction_description','transaction_amount','transaction_charge','transaction_type','receipt','account')
# admin.site.register(Transaction,TransactionAdmin)


# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ('message','date','customer','title')
#     search_fields = ('message','date','customer','title') 
# admin.site.register(Notification,NotificationAdmin)


# class RewardAdmin(admin.ModelAdmin):
#     list_display = ('transaction', 'customer','date_of_reward','points')
#     search_fields = ('transaction', 'customer','date_of_reward','points')
# admin.site.register(Reward,RewardAdmin)


# class ThirdPartyAdmin(admin.ModelAdmin):
#     list_display = ('account','transaction_amount','currency','date_of_issue','wallet','third_party_name','issuer')
#     search_fields = ('account','transaction_amount','currency','date_of_issue','wallet','third_party_name','issuer')
# admin.site.register(ThirdParty,ThirdPartyAdmin)


# class LoanAdmin(admin.ModelAdmin):
#     list_display = ('loan_id','loan_type','loan_balance','amount','guaranter','issuer','wallet')
#     search_fields = ('loan_id','loan_type','loan_balance','amount','guaranter','issuer','wallet')
# admin.site.register(Loan,LoanAdmin)




