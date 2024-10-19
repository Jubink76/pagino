from django.urls import path
from . import views

urlpatterns = [
    path('address_user/', views.address_detail, name='address_detail'),
]
