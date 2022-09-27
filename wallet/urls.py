import imp
from django.urls import path
from .views import register_card, register_customer, register_notification, register_reward,register_wallet,register_transaction,register_notification,register_currency,register_thirdparty,register_loan,register_receipt,list_customers,list_card,list_wallet,list_transaction,list_notifications,list_rewards,list_currency,list_thirdparty,list_loan,list_receipt
urlpatterns=[
    path("customer/",register_customer,name="registration"),
    path("card/",register_card,name="registration"),
    path("wallet/",register_wallet,name="registration"),
    path("transaction/",register_transaction,name="registration"),
    path("notify/",register_notification,name="registration"),
    path("reward/",register_reward,name="registration"),
    path("currency/",register_currency,name="registration"),
    path("thirdparty/",register_thirdparty,name="registration"),
    path("loan/",register_loan,name="registration"),
    path("receipt/",register_receipt,name="registration"),
    path("customer_list/",list_customers,name="registration"),
    path("card_list/",list_card,name="registration"),
    path("wallet_list/",list_wallet,name="registration"),
    path("transactions_list/",list_transaction,name="registration"),
    path("notification_list/",list_notifications,name="registration"),
    path("reward_list/",list_rewards,name="registration"),
    path("currency_list/",list_currency,name="registration"),
    path("thirdparty_list/",list_thirdparty,name="registration"),
    path("loan_list/",list_loan,name="registration"),
    path("receipt_list/",list_receipt,name="registration"),
]
