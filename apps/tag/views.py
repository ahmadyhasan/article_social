from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from apps.tag.serializers import TagSerializer

from apps.tag.models import Tag


class TagView(mixins.ListModelMixin, GenericViewSet,):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()
