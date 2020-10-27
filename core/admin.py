from django.contrib import admin
from .models import *


class MessageImageInline(admin.TabularInline):
    model = MessageImage
    extra = 0


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["date", "from_user", "to_user", "chat"]
    list_editable = ["chat"]
    inlines = [MessageImageInline]

admin.site.register(Chat)
admin.site.register(Parent)
admin.site.register(Child)
