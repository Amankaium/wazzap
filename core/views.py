from django.shortcuts import render, redirect
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


def add_message(request):
    if request.method == 'POST':
        chat_id = request.POST.get("chat")
        chat = Chat.objects.get(id=chat_id)
        text = request.POST.get("message")
        message = Message(
            chat=chat,
            text=text,
            from_user=request.user
        )
        message.save()
        return redirect(f'/chat/{ chat_id }#end')
    
    return redirect(homepage)


def google_map(request):
    return render(request, "map.html")