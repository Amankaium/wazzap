from django.shortcuts import render
from .models import Message


def homepage(request):
    messages = Message.objects.filter(to_user=request.user)
    return render(request, "homepage.html", {"messages": messages})
