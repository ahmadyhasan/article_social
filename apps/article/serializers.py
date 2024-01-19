from rest_framework import serializers
from apps.article.models import Article
from django.contrib.auth import get_user_model

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'content', 'create_time', 'update_time', 'is_publish')
        extra_kwargs = {'is_publish': {'read_only': True}, 'author': {'read_only': True}}

    def create(self, validated_data):
        user = self.context['request'].user

        user_info = User.objects.get(username=user)

        validated_data['author'] = [user_info.id]

        return super(ArticleSerializer, self).create(validated_data)
