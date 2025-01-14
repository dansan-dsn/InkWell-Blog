from django.urls import path
from .import views

urlpatterns = [
    path('create/', views.create_blog, name='create-blog'),
    path('fetch/', views.get_blogs, name='get-blogs'),
    path('fetch/<int:pk>/', views.get_blog, name='get-blog'),
    path('update/<int:pk>/', views.update_blog, name='update-blog'),
    path('delete/<int:pk>/', views.delete_blog, name='delete-blog'),
]