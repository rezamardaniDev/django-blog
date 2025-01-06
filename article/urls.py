from django.urls import path
from . import views

app_name = 'articles' 

urlpatterns = [
    path('', views.home_view, name='main'),
    path('<int:post_id>/view', views.post_view, name='detail')
]
