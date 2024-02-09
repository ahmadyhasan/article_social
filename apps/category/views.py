from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from apps.category.serializers import CategorySerializer

from apps.category.models import Category


class CategoryView(mixins.ListModelMixin, GenericViewSet,):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(all)
