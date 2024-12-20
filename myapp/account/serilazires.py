from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from myapp.account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Account


class AccountCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating or updating Account with hashed password.
    """

    class Meta:
        model = Account
        fields = '__all__'

    def create(self, validated_data):

        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

class AccountPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'guid',
            'first_name',
            'last_name',
            'middle_name'
        ]