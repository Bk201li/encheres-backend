from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user),
    path('user/', views.get_user),
    path('<str:pk>/update/', views.update_user),
]
