from rest_framework import serializers
from .models import ShoppingDb


class ShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingDb
        fields = ["id", "product", "done"]
