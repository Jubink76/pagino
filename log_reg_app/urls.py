from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage_before_login, name = 'homepage_before_login'),
    path('user_signup/',views.user_signup, name='user_signup'),
    path('user_login/',views.user_login, name='user_login'),
    path('homepage_after_login/',views.homepage_after_login, name='homepage_after_login'),
    path('user_logout',views.user_logout, name='user_logout'),
    path('admin_login',views.admin_login, name='admin_login'),
]