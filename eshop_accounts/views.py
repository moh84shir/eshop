from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView)
from django.urls import reverse_lazy
from django.views import generic

from .mixins import LoggedInRedirectMixin


class Login(LoggedInRedirectMixin, LoginView):
    pass


class Register(LoggedInRedirectMixin, generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/accounts/login/'


class Logout(LoginRequiredMixin, LogoutView):
    pass


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('accounts:password_change_done')


class PasswordChangeDone(PasswordChangeDoneView):
    pass
