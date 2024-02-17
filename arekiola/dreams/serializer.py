from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions
from .models import Post


class PostViewSetSerializer(ModelSerializer):

    def create(self, validated_data):
        # document = validated_data.get('document')  # read validated data
        post = Post.objects.create(**validated_data)  # saving post object
        return post

    class Meta:
        model = Post
        fields = '__all__'