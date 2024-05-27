from rest_framework import serializers

from apps.tag.models import Tag


class TagSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField()

    class Meta:
        model = Tag
        fields = ('slug',)

    @staticmethod
    def get_or_create_tags(tags: list):
        tags_objs = []
        for tag in tags:
            try:
                tag_obj = Tag.objects.get(slug=tag['slug'])
            except Tag.DoesNotExist:
                tag_obj = Tag.objects.create(slug=tag['slug'])

            tags_objs.append(tag_obj)

        return tags_objs
