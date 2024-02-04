from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserDetailSerializer


class CustomUserViewSets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer