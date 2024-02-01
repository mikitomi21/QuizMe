from rest_framework import serializers

from .models import CustomUser


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "username")

class UserCreateSerializer(serializers.ModelSerializer):
    pass
