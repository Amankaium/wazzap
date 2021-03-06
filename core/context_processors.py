from .models import Chat
from django.db.models import Q


def chats(request):
    if request.user.is_authenticated:
        chats = Chat.objects.filter(
            Q(message__from_user=request.user) |
            Q(message__to_user=request.user) |
            Q(users__in=[request.user])
        ).distinct()
    else:
        chats = []
    return {"chats": chats}