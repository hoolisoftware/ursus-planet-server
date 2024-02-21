from django.contrib import admin

from .models import User, UserEmailCode
from apps.wallets.models import UserWallet


class WalletInline(admin.TabularInline):
    model = UserWallet


class UserInline(admin.TabularInline):
    model = User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [WalletInline]
    list_display = (
        'username',
        'id',
        'email',
        'referrer',
        'points'
    )
    search_fields = (
        'username',
        'email'
    )
    autocomplete_fields = (
        'referrer',
    )


@admin.register(UserEmailCode)
class UserEmailCodeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'email',
        'code',
        'datetime_created'
    )
