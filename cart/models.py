from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    stock_pcs = models.IntegerField()
    price = models.IntegerField()
    shop_id = models.CharField(max_length=100)
    vip = models.BooleanField(default=True)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.IntegerField()
    shop_id  = models.CharField(max_length=100)
