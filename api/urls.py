from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewSet
from .views import WalletViewSet
from .views import AccountViewSet
from .views import CardViewSet
from .views import TransactionViewSet
from .views import LoanViewSet 
from .views import ReceiptViewSet 
from .views import NotificationViewSet 
from .views import AccountDepositView
router = routers.DefaultRouter()
router.register(r"customers",CustomerViewSet)
router.register(r"wallet",WalletViewSet)
router.register(r"account",AccountViewSet)
router.register(r"card",CardViewSet)
router.register(r"transaction",TransactionViewSet)
router.register(r"loan",LoanViewSet)
router.register(r"receipt",ReceiptViewSet)
router.register(r"notification",NotificationViewSet)
urlpatterns=[
    path("",include(router.urls)),
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
]