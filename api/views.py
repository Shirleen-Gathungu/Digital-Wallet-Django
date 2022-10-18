from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from wallet.models import Customer
from wallet.models import Wallet
from wallet.models import Account
from wallet.models import Card
from wallet.models import Loan
from wallet.models import Transaction
from wallet.models import Receipt
from wallet.models import Notification
from .serializers import CustomerSerializer
from .serializers import WalletSerializer
from .serializers import AccountSerializer
from .serializers import CardSerializer
from .serializers import TransactionSerializer
from .serializers import LoanSerializer
from .serializers import ReceiptSerializer
from .serializers import NotificationSerializer
# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset= Customer.objects.all()
    serializer_class =CustomerSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset= Wallet.objects.all()
    serializer_class =WalletSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset= Account.objects.all()
    serializer_class =AccountSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset= Card.objects.all()
    serializer_class =CardSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset= Transaction.objects.all()
    serializer_class =TransactionSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset= Loan.objects.all()
    serializer_class =LoanSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset= Receipt.objects.all()
    serializer_class =ReceiptSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset= Notification.objects.all()
    serializer_class =NotificationSerializer


class AccountDepositView(views.APIView):
   """
   This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)