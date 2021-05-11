from django.urls import path
from .views import home,Redirect,Info

urlpatterns = [
    path('', home, name="home"),
    path('info/', Info, name="info"),
    path("u/<str:slugs>/", Redirect, name="redirect")
]
