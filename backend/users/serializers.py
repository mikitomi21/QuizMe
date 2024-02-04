from rest_framework import serializers
from djoser.serializers import UserCreateMixin

from .models import CustomUser


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "username", "first_name", "last_name", "is_staff", "is_superuser")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "username")