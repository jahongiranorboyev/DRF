"""
 This is used to refer to APIVIEW
"""

from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.account.models import Account
from myapp.account.serilazires import AccountSerializer, AccountCreateSerializer, AccountPutSerializer


class AccountListAPIView(APIView):
    """
    View to list all accounts
    """

    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        """
        returns all accounts
        """

        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        adds a new account
        """
        serializer = AccountCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetailAPIView(APIView):
    """
    View to get a specific account or delete a specific account
    """

    def get_object(self, guid):
        try:
            return Account.objects.get(guid=guid)
        except Account.DoesNotExist:
            pass


    def get(self, request, guid, format=None):
        account = self.get_object(guid)
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, guid, format=None):
        account = self.get_object(guid)
        serializer = AccountPutSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, guid, format=None):
        account = self.get_object(guid)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


