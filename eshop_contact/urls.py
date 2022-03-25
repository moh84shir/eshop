from django.urls import path    

from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.ContactUs.as_view(), name='contact'),
    path('done/', views.ContactDone.as_view(), name='contact_done'),
]