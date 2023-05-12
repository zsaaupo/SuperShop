from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView

urlpatterns = [
    path('registerapi/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('loginapi/', UserLoginAPIView.as_view(), name='user-login'),
]