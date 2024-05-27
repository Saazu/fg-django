# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import CustomUser, AccountBalance, PhoneNumber
from .forms import CustomUserChangeForm, CustomUserCreationForm


class AccountBalanceAdmin(admin.ModelAdmin):
    list_display = ("user", "main_balance", "bonus_balance", "updated_at")


admin.site.register(AccountBalance, AccountBalanceAdmin)


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "main_phone_number",
        "momo_phone_number",
        "updated_at",
    )


admin.site.register(PhoneNumber, PhoneNumberAdmin)


class AccountBalanceInline(admin.TabularInline):
    model = AccountBalance


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    list_display = ("username", "email", "total_winnings", "name", "is_staff")
    search_fields = ("username", "email")
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("total_winnings",)}),)
    add_fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("total_winnings",)}),)
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    inlines = [AccountBalanceInline, PhoneNumberInline]


admin.site.register(CustomUser, CustomUserAdmin)
