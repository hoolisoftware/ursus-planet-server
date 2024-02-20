from django.contrib import admin

from .models import User, UserEmailCode
from apps.wallets.models import UserWallet


class WalletInline(admin.TabularInline):
    model = UserWallet


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [WalletInline]
    list_display = (
        'username',
        'id',
        'email',
        'points'
    )
    search_fields = (
        'username',
        'email'
    )


@admin.register(UserEmailCode)
class UserEmailCodeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'email',
        'code',
        'datetime_created'
    )
