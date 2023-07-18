from rest_framework import serializers
from .models import WalletListDb


class WalletListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletListDb
        fields = ["id", "female", "person", "price"]
