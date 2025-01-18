from django.urls import path
from . import views

urlpatterns = [
    path('fetch/', views.list_media, name='list_media'),
    path('create/', views.create_media, name='create_media'),
    path('fetch/<int:pk>/', views.retrieve_media, name='retrieve_media'),
    path('<int:pk>/update/', views.update_media, name='update_media'),
    path('<int:pk>/delete/', views.delete_media, name='delete_media'),
]
