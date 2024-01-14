from rest_framework import serializers
from apps.article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'content', 'create_time', 'update_time', 'is_publish')
        extra_kwargs = {'is_publish': {'read_only': True}}
