from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView

from .models import Contact


class ContactUs(LoginRequiredMixin, CreateView):
    model = Contact
    fields = '__all__'
    success_url = '/contact/done/'


class ContactDone(LoginRequiredMixin, TemplateView):
    template_name = 'eshop_contact/contact_done.html'
