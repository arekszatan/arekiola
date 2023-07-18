from rest_framework import serializers
from .models import ShoppingOtherDb


class ShoppingOtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingOtherDb
        fields = ["id", "product", "done"]
