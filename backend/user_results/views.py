from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import PlayerResultOfQuiz
from .serializers import ResultSerializer
from users.models import CustomUser

# Create your views here.


class ResultDetailView(generics.RetrieveAPIView):
    queryset = PlayerResultOfQuiz.objects.all()
    serializer_class = ResultSerializer


class UserResultDetailView(generics.RetrieveAPIView):
    serializer_class = ResultSerializer
    print("siema1")

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        print("siema2")
        return PlayerResultOfQuiz.objects.filter(user__id=pk)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print("siema3")
        print(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ResultListView(generics.ListAPIView):
    queryset = PlayerResultOfQuiz.objects.all()
    serializer_class = ResultSerializer


class ResultCreateView(generics.CreateAPIView):
    queryset = PlayerResultOfQuiz.objects.all()
    serializer_class = ResultSerializer

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content")
        print(content)
