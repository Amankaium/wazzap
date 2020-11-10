from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory, modelformset_factory
from .models import Profile
from .forms import *
from .mixins import ProfileOwnerMixin

# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    template_name = "userprofile/profile.html"
    queryset = Profile.objects.all()


class ProfileFormView(FormView):
    template_name = "userprofile/profile_form.html"
    form_class = ProfileUpdateForm
    success_url = "/"


class ProfileUpdateView(ProfileOwnerMixin, UpdateView):
    model = Profile
    fields = ["photo"]
    success_url = "/"
    template_name = "userprofile/profile_update_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_form"] = UserForm(instance=self.request.user)
        context["social_link_formset"] = modelformset_factory(
            ProfileSocialLink,
            exclude=("id",),
            extra=2
        )

        # context["social_link_formset"] = formset_factory(SocialLinkForm, extra=3)

        return context
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.request.user
        form = request.POST
        
        user.username = form["username"]
        user.first_name = form["first_name"]
        user.last_name = form["last_name"]
        user.save()

        SocialLinkFormSet = modelformset_factory(
            ProfileSocialLink,
            exclude=("id",)
        )
        formset = SocialLinkFormSet(form)
        if formset.is_valid():
            formset.save()

        # SocialLinkFormSet = formset_factory(SocialLinkForm, min_num=2, validate_min=True)
        # formset = SocialLinkFormSet(form)
        # print(formset.is_valid())

        return response


