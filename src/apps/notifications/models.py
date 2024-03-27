from django.db import models


class AbstractUserWithNotificationSettings(models.Model):

    class Meta:
        abstract = True

    FREQUENCY_CHOICES = (
        ('fast', 'As fast as possible'),
        ('hour', 'Every hour'),
        ('day', 'Every day'),
        ('week', 'Every week'),
        ('month', 'Every month')
    )

    cabinet_notifications_email = models.BooleanField(default=False)
    cabinet_notifications_account = models.BooleanField(default=False)
    cabinet_notifications_frequency = models.CharField(
        choices=FREQUENCY_CHOICES,
        max_length=64,
        default='fast'
    )

    project_notifications_email = models.BooleanField(default=False)
    project_notifications_account = models.BooleanField(default=False)
    project_notifications_frequency = models.CharField(
        choices=FREQUENCY_CHOICES,
        max_length=64,
        default='fast'
    )
