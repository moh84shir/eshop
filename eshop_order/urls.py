from django.urls import path

from . import views


urlpatterns = [
    path('verify/<order_id>/', views.verify, name='verify'),
    path('add-user-order/', views.add_user_order),
    path('request/', views.send_request, name='request'),
    path('open-order/', views.user_open_order),
    path('remove-order-detail/<detail_id>/', views.remove_order_detail),
]
