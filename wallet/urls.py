import imp
from django.urls import path
from .views import register_card, register_customer, register_notification, register_reward,register_wallet,register_transaction,register_notification,register_currency,register_thirdparty,register_loan,register_receipt
urlpatterns=[
    path("register/",register_customer,name="registration"),
    path("display/",register_card,name="registration"),
    path("show/",register_wallet,name="registration"),
    path("render/",register_transaction,name="registration"),
    path("notify/",register_notification,name="registration"),
    path("reward/",register_reward,name="registration"),
    path("currency/",register_currency,name="registration"),
    path("thirdparty/",register_thirdparty,name="registration"),
    path("loan/",register_loan,name="registration"),
    path("receipt/",register_receipt,name="registration"),
]
