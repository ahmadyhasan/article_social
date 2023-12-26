from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, filters
from apps.article.serializers import RegistrationSerializer, ArticleSerializer

from apps.article.models import Article


class ArticleView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author', 'title']

    def get_queryset(self):
        return Article.objects.filter(is_publish=True)
