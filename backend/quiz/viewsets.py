from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        quiz = serializer.validated_data.get('quiz')

        if quiz is None:
            return Response({"error": "Quiz is not found"}, status.HTTP_404_NOT_FOUND)

        serializer.save(quiz=quiz)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        question = serializer.validated_data.get('question')

        if question is None:
            return Response({"error": "Question is not found"}, status.HTTP_404_NOT_FOUND)
        serializer.save(question=question)
