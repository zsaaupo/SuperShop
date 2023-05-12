from django.urls import path
from .views import SalesAPIView, SalesEditAPIView

urlpatterns = [
    path('sales/', SalesAPIView.as_view(), name='sales-api'),
    path('sales/<str:id>/', SalesEditAPIView.as_view(), name='sales-edit-api'),
]