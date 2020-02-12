from rest_framework import serializers
from cats.models import Category

class SimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class CategorySerializer(serializers.ModelSerializer):
    parents = SimpleSerializer(
        many=True,
        read_only=True
    )
    children = SimpleSerializer(
        many=True,
        read_only=True
    )
    siblings = SimpleSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'parents', 'children', 'siblings')