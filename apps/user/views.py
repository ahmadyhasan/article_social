from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.translation import gettext as _
from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from apps.user.serializers import RegistrationSerializer, UserSerializer

User = get_user_model()


class UserView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(is_active=True)


class RegistrationView(APIView):
    @extend_schema(request=RegistrationSerializer)
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            email = serializer.validated_data['email']

            user = User.objects.create(
                username=serializer.validated_data['username'],
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                email=email,
                is_active=True,
            )
            user.set_password(serializer.validated_data['password'])
            user.save()

        return Response(_('Create an user'))
