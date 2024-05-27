from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

# Create your views here.
from .models import PhoneNumber, AccountBalance, CustomUser
from .serializers import (
    PhoneNumberSerializer,
    AccountBalanceSerializer,
    CustomeUserSerializer,
)


class PhoneNumberViewset(viewsets.ViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class AccountBalanceViewset(viewsets.ViewSet):
    queryset = AccountBalance.objects.all()
    serializer_class = AccountBalanceSerializer


class CustomUserViewset(viewsets.ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomeUserSerializer
