from rest_framework import generics
from .serializers import SalesSerializer
from .models import Sales

class SalesAPIView(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer