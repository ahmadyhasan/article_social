from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField()

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise ValidationError(_('Passwords are not match with each other'))

        return attrs

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'password_confirm')
