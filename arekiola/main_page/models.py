from django.db import models


class ShoppingList(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    data_time = models.DateTimeField(auto_now_add=True)
    things_to_buy = models.CharField(max_length=300)
    checked = models.BooleanField()
    finished = models.BooleanField()


class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
