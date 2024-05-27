from rest_framework import serializers
from .models import AccountBalance, PhoneNumber, CustomUser


class AccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountBalance
        fields = "__all__"
        read_only_fields = ("main_balance", "bonus_balance")


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = "__all__"
        read_only_fields = ("main_phone_number", "momo_phone_number")


class CustomeUserSerializer(serializers.ModelSerializer):
    model = CustomUser
    fields = "__all__"
