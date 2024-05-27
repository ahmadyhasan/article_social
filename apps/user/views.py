from django.contrib.auth import get_user_model
from rest_framework import mixins, filters
from rest_framework.viewsets import GenericViewSet
from apps.user.serializers import RegistrationSerializer, UserSerializer

User = get_user_model()


class UserView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']

    def get_queryset(self):
        return User.objects.filter(is_active=True)


class RegistrationView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = RegistrationSerializer
