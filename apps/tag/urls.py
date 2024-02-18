from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.tag.views import TagView

_API_ROUTER = DefaultRouter()

_API_ROUTER.register('api/v1/tag', TagView, basename='tags')

urlpatterns = (
    path('', include(_API_ROUTER.urls)),
)
