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


class CustomUserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberSerializer()
    account_balance = AccountBalanceSerializer()

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "name",
            "email",
            "phone_number",
            "account_balance",
            "total_winnings",
        )
