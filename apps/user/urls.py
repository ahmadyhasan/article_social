from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.user.views import RegistrationView, UserView

_API_ROUTER = DefaultRouter()

_API_ROUTER.register('/users', UserView, basename='users')
_API_ROUTER.register('/Registration', RegistrationView, basename='Registration')

urlpatterns = (
    path('api/v1', include(_API_ROUTER.urls)),
)
