from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('products/', views.getProducts),
    path('products/create/', views.createProduct),
    path('products/<str:pk>/update', views.updateProduct),
    path('products/<str:pk>/delete', views.deleteProduct),
    path('products/<str:pk>/', views.getProduct), 
]