from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register-user'),
    path('login/', views.login, name='login-user'),
    path('get_user/<int:pk>/', views.get_user, name='get-user'),
    path('get_all_users/', views.all_users, name='all-user'),
    path('update_user/<int:pk>/', views.update_user, name='update-user'),

    path('delete_user/<int:pk>/', views.delete_user, name='delete-user'),
]