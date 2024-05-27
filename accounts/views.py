from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.contrib.auth import get_user_model

# Create your views here.
from .models import PhoneNumber, AccountBalance, CustomUser
from .serializers import (
    PhoneNumberSerializer,
    AccountBalanceSerializer,
    CustomeUserSerializer,
)
from .permissions import IsAuthorOrAdmin


class PhoneNumberViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrAdmin]
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class AccountBalanceViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrAdmin]
    queryset = AccountBalance.objects.all()
    serializer_class = AccountBalanceSerializer


class CustomUserViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrAdmin]
    queryset = get_user_model().objects.prefetch_related(
        "phone_number", "account_balance"
    )
    serializer_class = CustomeUserSerializer
    filterset_fields = ("phone_number", "email")
