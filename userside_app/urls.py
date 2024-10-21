from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_before_login, name='homepage_before_login'),
    path('homepage_after_login/',views.homepage_after_login, name='homepage_after_login'),
    path('all_products/',views.all_products, name='all_products'),
    path('single_product/',views.single_product, name='single_product'),
]
