from django.db import models


class Sales(models.Model):
    
    id = models.IntegerField(unique=True, primary_key=True)
    order_id = models.CharField(max_length=30, null=True, blank=True, unique=True)
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=30, null=True, blank=True)
    customer_id = models.CharField(max_length=30, null=True, blank=True, unique=True)
    customer_name = models.CharField(max_length=30, null=True, blank=True)
    segment = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    postal_code = models.CharField(max_length=30, null=True, blank=True)
    region = models.CharField(max_length=30, null=True, blank=True)
    product_id = models.CharField(max_length=30, null=True, blank=True)
    catagory = models.CharField(max_length=30, null=True, blank=True)
    sub_catagory = models.CharField(max_length=30, null=True, blank=True)
    product_name = models.CharField(max_length=30, null=True, blank=True)
    sales = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.order_id