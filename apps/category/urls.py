from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.category.views import CategoryView

_API_ROUTER = DefaultRouter()

_API_ROUTER.register('api/v1/category', CategoryView, basename='categories')

urlpatterns = (
    path('', include(_API_ROUTER.urls)),
)
