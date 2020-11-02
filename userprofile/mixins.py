from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

class ProfileOwnerMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(id=kwargs["pk"])
        if request.user != profile.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
