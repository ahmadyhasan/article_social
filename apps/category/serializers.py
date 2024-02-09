from rest_framework import serializers
from apps.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
        extra_kwargs = {'name': {'read_only': True}}
