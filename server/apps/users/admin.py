from django.contrib import admin

from .models import User
from apps.wallets.models import UserWallet


class WalletInline(admin.TabularInline):
    model = UserWallet


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [WalletInline]
    list_display = (
        'username',
        'email',
    )
    search_fields = (
        'username',
        'email'
    )
