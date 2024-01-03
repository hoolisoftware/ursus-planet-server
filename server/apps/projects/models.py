from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} ({self.id})"
        
