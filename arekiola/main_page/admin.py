from django.contrib import admin
from .models import ShoppingList, CartItem

admin.site.register(ShoppingList)
admin.site.register(CartItem)
