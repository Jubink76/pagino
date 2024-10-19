from django.urls import path,include
from . import views
urlpatterns = [
    path('admin_users/',views.admin_users, name='admin_users'),
]