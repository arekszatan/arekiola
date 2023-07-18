from rest_framework import serializers
from .models import ColorDb


class ColorDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorDb
        fields = ["id", "name", "textColor"]
