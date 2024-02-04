from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Quiz, Question, Answer
from users.models import CustomUser
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer
from users.serializers import UserSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)

    @action(
        methods=["GET"],
        detail=True
    )
    def questions(self, request, pk=None):
        quiz = self.get_object()
        questions = Question.objects.filter(quiz=quiz)
        serializer = QuestionSerializer(questions, many=True)

        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        quiz = serializer.validated_data.get('quizzes')
        print(quiz)

        if quiz is None:
            return Response({"error": "Quiz is not found"}, status.HTTP_404_NOT_FOUND)

        serializer.save(quiz=quiz)

    @action(
        methods=["GET"],
        detail=True
    )
    def answers(self, request, pk=None):
        question = self.get_object()
        answers = Answer.objects.filter(question=question)
        answers_serializer = AnswerSerializer(answers, many=True)

        return Response(answers_serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        question = serializer.validated_data.get('question')

        if question is None:
            return Response({"error": "Question is not found"}, status.HTTP_404_NOT_FOUND)
        serializer.save(question=question)
