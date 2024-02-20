# from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

# from apps.tasks.models import PlatformTaskLog, PlatformTaskSettings
from .. import models


# User = get_user_model()


def create_social_handler(social, social_task_name):
    @receiver(pre_save, sender=social)
    def handler(sender, instance, **kwargs):
        print('social created')
        print(social_task_name)

    return handler


handler_discord = create_social_handler(models.SocialAccountDiscord, 'task_social_discord')
handler_telegram = create_social_handler(models.SocialAccountTelegram, 'task_social_telegram')
handler_github = create_social_handler(models.SocialAccountGithub, 'task_social_github')
handler_x = create_social_handler(models.SocialAccountX, 'task_social_x')
