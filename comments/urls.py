from django.urls import path
from .import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('fetch/', views.get_all, name='get-all'),
    path('fetch/<int:pk>/', views.get_comment, name='get-comment'),
    path('update_comment/<int:pk>/', views.update_comment, name='update-comment'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete-comment'),
]