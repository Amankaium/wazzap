from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    from_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    to_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

