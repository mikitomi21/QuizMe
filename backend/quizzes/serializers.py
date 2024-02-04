from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = ("id", "author", "title", "description", "created", "updated")


class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ("id", "quiz", "text", "question_type")


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ("id", "question", "text", "is_correct")
