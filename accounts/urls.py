from rest_framework import routers

from .views import CustomUserViewset, AccountBalanceViewset, PhoneNumberViewset

router = routers.SimpleRouter()
router.register("", CustomUserViewset, basename="users")
router.register("phone_numbers", PhoneNumberViewset, basename="phone_numbers")
router.register("account_balance", AccountBalanceViewset, basename="account_balances")


urlpatterns = router.urls
