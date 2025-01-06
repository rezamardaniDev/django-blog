from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/view_user', views.profile, name='get-uesr')
]
