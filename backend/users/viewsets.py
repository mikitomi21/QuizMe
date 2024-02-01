from rest_framework import viewsets

from .models import CustomUser
from .serializers import UserDetailSerializer


class CustomUserViewSets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
