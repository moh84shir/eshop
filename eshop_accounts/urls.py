from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('password-change/', views.PasswordChange.as_view(), name='password_change'),
    path('password-change-done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
]