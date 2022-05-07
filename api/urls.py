from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('products/', views.get_products),
    path('products/create/', views.create_product),
    path('products/<str:pk>/update', views.update_product),
    path('products/<str:pk>/delete', views.delete_product),
    path('products/<str:pk>/', views.get_product),
]