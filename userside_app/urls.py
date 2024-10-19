from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage_without_user, name='home_without_user'),
]
