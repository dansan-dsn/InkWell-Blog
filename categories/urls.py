from django.urls import path
from .import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('fetch/', views.get_all, name='get-all'),
    path('fetch/<int:pk>/', views.get_category, name='get-category'),
    path('update_category/<int:pk>/', views.update_category, name='update-category'),
    path('delete_category/<int:pk>/', views.delete_category, name='delete-category'),
]