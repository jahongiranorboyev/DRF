"""
Viewset is used here
"""
from rest_framework import viewsets

from myapp.account.models import Account
from myapp.account.serilazires import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
