from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.db import transaction

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(max_length=100, write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'password_confirm')
        extra_kwargs = {"password": {"write_only": True}, "id": {"read_only": True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise ValidationError(_('Passwords are not match with each other'))
        else:
            try:
                validate_password(attrs['password'])
            except ValidationError as exc:
                raise serializers.ValidationError(str(exc))
        del attrs['password_confirm']

        return attrs

    def create(self, validated_data):
        with transaction.atomic():

            user = super(RegistrationSerializer, self).create(validated_data)
            user.set_password(validated_data['password'])
            user.save()

        return user
