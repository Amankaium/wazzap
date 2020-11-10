from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ProfileSocialLink)

class SocialLinkInline(admin.TabularInline):
    exclude = ["id"]
    model = ProfileSocialLink

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]

