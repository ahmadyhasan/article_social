from django.contrib import admin

from apps.article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_author', 'is_publish')
