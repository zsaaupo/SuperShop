from rest_framework import serializers
from .models import Sales

class SalesSerializer(serializers.ModelSerializer):
    sales = serializers.SerializerMethodField()


    def get_id(self, instance):
        id = instance.id
        return int(id) if id else None
    
    
    def get_sales(self, instance):
        sales = instance.sales
        return int(sales) if sales else None

    class Meta:
        model = Sales
        fields = '__all__'