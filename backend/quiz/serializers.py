from rest_framework import serializers
from .models import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("id", "title", "description", "created", "updated")


class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer

    class Meta:
        model = Question
        fields = ("id", "quiz", "text")


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer

    class Meta:
        model = Answer
        fields = ("id", "question", "text", "is_correct")
