from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["id"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]