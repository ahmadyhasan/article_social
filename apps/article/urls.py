from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.article.views import ArticleView

_API_ROUTER = DefaultRouter()

_API_ROUTER.register('/articles', ArticleView, basename='articles')

urlpatterns = (
    path('api/v1', include(_API_ROUTER.urls)),
)
