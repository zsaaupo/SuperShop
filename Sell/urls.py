from django.urls import path
from .views import SalesAPIView

urlpatterns = [
    path('sales/', SalesAPIView.as_view(), name='sales-api'),
]