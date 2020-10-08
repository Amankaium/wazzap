from django.contrib import admin
from .models import *


class MessageImageInline(admin.TabularInline):
    model = MessageImage
    extra = 0


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["date", "from_user", "to_user"]
    inlines = [MessageImageInline]




