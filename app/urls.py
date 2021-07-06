from django.urls import path
from .views import home,Redirect,Info,updateItem, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('info/', Info, name="info"),
    path('update_item/', updateItem, name="update"),
    path("u/<str:slugs>/", Redirect, name="redirect"),


    path('login/',auth_views.LoginView.as_view(template_name="app/login.html"), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name="app/logout.html"), name='logout'),

    # for reference in future
    # path('password-reset/',auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('password-reset/done/',auth_views.PasswordChangeDoneView.as_view(), name="password_reset_done"),
    # path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    # path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),


    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_rest_confirm.html"),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name="password_reset_complete"),
]
