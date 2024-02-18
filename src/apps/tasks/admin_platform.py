from django.contrib import admin


class LogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'reward',
        'got'
    )


class TaskSocialXLogAdmin(LogAdmin):
    pass


class TaskSocialGithubLogAdmin(LogAdmin):
    pass


class TaskSocialDiscordLogAdmin(LogAdmin):
    pass


class TaskSocialTelegramLogAdmin(LogAdmin):
    pass


class TaskEmailLogAdmin(LogAdmin):
    pass


class TaskUsernameLogAdmin(LogAdmin):
    pass


class TaskDomainIdLogAdmin(LogAdmin):
    pass


class TaskAvatarLogAdmin(LogAdmin):
    pass


class TaskNftAvatarLogAdmin(LogAdmin):
    pass


class TaskUrsasCollectionNftAvatarLogAdmin(LogAdmin):
    pass


class TaskWalletLogAdmin(LogAdmin):
    pass


class TaskChainLogAdmin(LogAdmin):
    pass


class TaskReferralSelfLogAdmin(LogAdmin):
    pass


class TaskEmailNotificationLogAdmin(LogAdmin):
    pass


class TaskCabinetNotificationLogAdmin(LogAdmin):
    pass
