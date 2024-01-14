from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, filters
from apps.article.serializers import ArticleSerializer

from apps.article.models import Article


class ArticleView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author', 'title']

    def get_queryset(self):
        return Article.objects.filter(is_publish=True)
