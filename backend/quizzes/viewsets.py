from django.shortcuts import get_object_or_404

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

    @action(methods=["GET"], detail=True)
    def get_questions(self, request, pk=None):
        quiz = get_object_or_404(Quiz, id=pk)
        questions = Question.objects.filter(quiz=quiz)
        serializer = QuestionSerializer(questions, many=True)

        return Response(serializer.data)

    @action(methods=["POST"], detail=True)
    def post_question(self, request, pk=None):
        quiz = get_object_or_404(Quiz, id=pk)

        question_serializer = QuestionSerializer(data=request.data)
        if question_serializer.is_valid():
            question_serializer.validated_data["quiz"] = quiz
            question_serializer.save()
            return Response(
                {"message": f"Question is added to the quiz nr.{quiz.id}"},
                status=status.HTTP_201_CREATED,
            )
        return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        quiz = serializer.validated_data.get("quizzes")

        if quiz is None:
            return Response({"error": "Quiz is not found"}, status.HTTP_404_NOT_FOUND)

        serializer.save(quiz=quiz)

    @action(methods=["GET"], detail=True)
    def get_answers(self, request, pk=None):
        question = get_object_or_404(Question, id=pk)
        answers = Answer.objects.filter(question=question)
        answers_serializer = AnswerSerializer(answers, many=True)

        return Response(answers_serializer.data)

    @action(methods=["POST"], detail=True)
    def post_answer(self, request, pk=None):
        question = get_object_or_404(Question, id=pk)

        answer_serializer = AnswerSerializer(data=request.data)
        if answer_serializer.is_valid():
            answer_serializer.validated_data["question"] = question
            answer_serializer.save()
            return Response(
                {"message": f"Answer is added to the question nr.{question.id}"},
                status=status.HTTP_201_CREATED,
            )
        return Response(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        question = serializer.validated_data.get("question")

        if question is None:
            return Response(
                {"error": "Question is not found"}, status.HTTP_404_NOT_FOUND
            )
        serializer.save(question=question)
