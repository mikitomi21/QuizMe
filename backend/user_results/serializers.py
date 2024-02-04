from rest_framework import serializers

from users.serializers import UserSerializer
from quizzes.serializers import QuizSerializer
from .models import PlayerResultOfQuiz


class ResultSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PlayerResultOfQuiz
        fields = ("user", "quiz", "attempt", "correct_answers", "wrong_answers")
