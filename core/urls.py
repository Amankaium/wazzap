from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage),
    path("chat/<int:id>/", chat, name="chat"),
    path("add-message/", add_message, name='add-message'),
    path("map/", google_map, name="map")
]