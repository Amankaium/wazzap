from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='profile',
        verbose_name='Пользователь',
    )

    vk = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
