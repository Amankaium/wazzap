from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    from_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )

    to_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="received_messages"
    )


class MessageImage(models.Model):
    message = models.ForeignKey(
        to=Message,
        on_delete=models.CASCADE,
        related_name="message_image"
    )

    image = models.ImageField(
        upload_to="messages/"
    )