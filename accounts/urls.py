from django.urls import path
from rest_framework import routers

from .views import CustomUserViewset, AccountBalanceViewset, PhoneNumberViewset

router = routers.SimpleRouter()
router.register("users", CustomUserViewset, basename="users")
