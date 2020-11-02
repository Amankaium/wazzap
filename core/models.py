from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    users = models.ManyToManyField(
        to=User,
        blank=True,
        verbose_name="участники"
    )

    def __str__(self):
        return self.name


class Message(models.Model):
    chat = models.ForeignKey(
        Chat, models.SET_NULL,
        null=True,
        related_name="message" 
    )
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    from_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )

    to_user = models.ForeignKey(
        to=User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="received_messages"
    )

    class Meta:
        ordering = ["date"]

class MessageImage(models.Model):
    message = models.ForeignKey(
        to=Message,
        on_delete=models.CASCADE,
        related_name="message_image"
    )

    image = models.ImageField(
        upload_to="messages/"
    )


class Parent(models.Model):
    test_attr = models.CharField(max_length=10)


class Child(Parent):
    test_attr_2 = models.IntegerField()