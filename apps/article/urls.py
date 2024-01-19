from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.article.views import ArticleView

_API_ROUTER = DefaultRouter()

_API_ROUTER.register('api/v1/articles', ArticleView, basename='articles')

urlpatterns = (
    path('', include(_API_ROUTER.urls)),
)
