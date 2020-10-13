from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage),
    path("chat/<int:id>/", chat, name="chat")
]