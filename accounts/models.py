from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class PhoneNumber(models.Model):
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    main_phone_number = models.CharField(max_length=12)
    momo_phone_number = models.CharField(max_length=12)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "Phone number: {} Momo number: {}".format(
            self.main_phone_number, self.momo_phone_number
        )


class AccountBalance(models.Model):
    user = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    main_balance = models.IntegerField(default=0)
    bonus_balance = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "Main balance: {},  Bonus balance{}".format(
            self.main_balance, self.bonus_balance
        )


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    created_at = models.TimeField(auto_now_add=True)
    total_winnings = models.IntegerField(default=0)
    phone_number = models.OneToOneField(
        "PhoneNumber",
        related_name="phone_number",
        on_delete=models.CASCADE,
        unique=True,
    )
    account_balance = models.OneToOneField(
        "AccountBalance",
        related_name="account_balanace",
        on_delete=models.CASCADE,
        unique=True,
    )
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ["phone_number", "account_balance"]
