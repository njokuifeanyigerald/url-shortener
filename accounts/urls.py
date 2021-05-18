from django.shortcuts import redirect
from django.urls import path

from .views import LoginView, RegisterView,logoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', LoginView.as_view( redirect_authenticated_user=True), name='login'),
    path('logout/', logoutView, name='logout'),
    # if request.user.is_authenticated:
        path('register/', RegisterView.as_view(), name='register'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


# path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html", redirect_authenticated_user=True), name='login'),
]
