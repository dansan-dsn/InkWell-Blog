from django.urls import path
from .import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('fetch/', views.get_all, name='get-all'),
    path('fetch/<int:pk>/', views.get_reaction, name='get-reaction'),
    path('update_reaction/<int:pk>/', views.update_reaction, name='update-reaction'),
    path('delete_reaction/<int:pk>/', views.delete_reaction, name='delete-reaction'),
]