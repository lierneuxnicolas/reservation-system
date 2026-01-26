
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserSignUpForm

from django.contrib.auth.decorators import login_required
from catalogue.models import UserMeta

class UserSignUpView(UserPassesTestMixin, CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def test_func(self):
        return self.request.user.is_anonymous or \
               self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "Vous êtes déjà inscrit!")
        return redirect('home')

@login_required
def profile(request):
    languages = {
        "fr": "Français",
        "en": "English",
        "nl": "Nederlands",
    }
    usermeta, created = UserMeta.objects.get_or_create(user=request.user, defaults={"langue": "fr"})
    return render(request, 'user/profile.html', {
        "user_language" : languages.get(usermeta.langue, "Français"),
    })
