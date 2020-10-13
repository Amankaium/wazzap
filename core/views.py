from django.shortcuts import render
from django.db.models import Q
from .models import *


def homepage(request):
    # messages = Message.objects.filter(to_user=request.user)
    chats = Chat.objects.filter(
        Q(message__from_user=request.user) |
        Q(message__to_user=request.user)
    ).distinct()
    return render(request, "homepage.html", {"chats": chats})


def chat(request, id):
    chat_object = Chat.objects.get(id=id)
    context = {"chat": chat_object}
    return render(request, "chat.html", context)