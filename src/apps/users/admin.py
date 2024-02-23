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
        'points',
        'points_referral',
    )
    search_fields = (
        'username',
        'email'
    )
    autocomplete_fields = (
        'referrer',
    )
    fieldsets = (
        ('General', {
            "fields": (
                'username',
                'email',
                'avatar',
            ),
        }),
        ('Points & referrer', {
            "fields": (
                'points',
                'points_referral',
                'referrer',
                'referral_quote',
            ),
        }),
        ('Notifications', {
            "fields": (
                'cabinet_notifications_email',
                'cabinet_notifications_account',
                'cabinet_notifications_frequency',
                'project_notifications_email',
                'project_notifications_account',
                'project_notifications_frequency'
            ),
        }),
        ('Groups & permissions', {
            "fields": (
                'user_permissions',
                'groups',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


@admin.register(UserEmailCode)
class UserEmailCodeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'email',
        'code',
        'datetime_created'
    )
