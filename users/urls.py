
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('recover-password/', views.forgot_password, name='recover-password'),
    path('logout/', views.logout_view, name='logout'),
]
