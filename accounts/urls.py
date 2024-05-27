from rest_framework import routers

from .views import CustomUserViewset, AccountBalanceViewset, PhoneNumberViewset

router = routers.SimpleRouter()
router.register("users", CustomUserViewset, basename="users")
router.register("users/phone_numbers", PhoneNumberViewset, basename="phone_numbers")
router.register(
    "users/account_balance", AccountBalanceViewset, basename="account_balances"
)


urlpatterns = router.urls
