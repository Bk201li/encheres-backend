from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.get_routes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', views.get_products),
    path('products/create/', views.create_product),
    path('products/<str:pk>/update/', views.update_product),
    path('products/<str:pk>/delete/', views.delete_product),
    path('products/<str:pk>/', views.get_product),
    path('auctions/create/', views.create_auctions),
]