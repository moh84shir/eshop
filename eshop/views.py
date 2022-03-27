from django.shortcuts import render
from django.views.generic import TemplateView
from eshop_settings.models import Setting


def index(request):
    if not Setting.objects.last():
        Setting.objects.create(title='بامبولا')
    settings = Setting.objects.last()
    return render(request, 'index.html', {'settings':settings})
