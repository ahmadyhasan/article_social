from rest_framework import serializers
from django.db import transaction
from apps.article.models import Article
from apps.tag.serializers import TagSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = \
            (
                'id',
                'author',
                'category',
                'title',
                'content',
                'tags',
                'create_time',
                'update_time',
                'is_publish',
            )
        extra_kwargs = {'is_publish': {'read_only': True}, 'author': {'read_only': True}}

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        with transaction.atomic():
            user = self.context['request'].user
            user_info = User.objects.get(username=user)
            validated_data['author'] = [user_info.id]

            article_obj = super().create(validated_data)
            tags_objs = TagSerializer.get_or_create_tags(tags)
            article_obj.tags.set(tags_objs)

        return article_obj
