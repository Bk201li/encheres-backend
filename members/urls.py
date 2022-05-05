from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    # path('', getRoutesView.as_view() name='routes'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
