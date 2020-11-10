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

    photo = models.ImageField(
        upload_to="profile/",
        null=True, blank=True
    )


class ProfileSocialLink(models.Model):
    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="social_link"
    )

    name = models.CharField(max_length=55)
    link = models.CharField(max_length=55)