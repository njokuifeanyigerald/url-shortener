from django.urls import path
from .views import home,Redirect,Info,updateItem

urlpatterns = [
    path('', home, name="home"),
    path('info/', Info, name="info"),
    path('update_item/', updateItem, name="update"),
    path("u/<str:slugs>/", Redirect, name="redirect")
]
