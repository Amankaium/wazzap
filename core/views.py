from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.mail import send_mail
from wazzap.settings import key
# from django.conf import key
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
        
        users = User.objects.filter(sent_messages__chat=chat).exclude(id=request.user.id)
        emails = [user.email for user in users] # if user != request.user]

        send_mail(
            subject="Вам пришло новое сообщение",
            message=f"Текст сообщения: {text}\nОт пользователя: {request.user.username}",
            from_email=request.user.email,
            recipient_list=emails
        )

        return redirect(f'/chat/{ chat_id }#end')
    
    return redirect(homepage)


def google_map(request):
    return render(request, "map.html", {"key": key})

def two_gis(request):
    return render(request, "two_gis.html")