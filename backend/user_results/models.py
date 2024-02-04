from django.db import models
from users.models import CustomUser
from quizzes.models import Quiz


# Create your models here.


class PlayerResultOfQuiz(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    attempt = models.IntegerField(default=1)
    correct_answers = models.IntegerField(default=0)
    wrong_answers = models.IntegerField(default=0)

    def percent_of_result(self) -> float:
        if not self.correct_answers or not self.wrong_answers:
            return 0
        return self.correct_answers / (self.correct_answers + self.wrong_answers) * 100

    def correct_answer(self, points: int = 1):
        self.correct_answers += points

    def wrong_answer(self, points: int = 1):
        self.wrong_answers += points

    def __str__(self):
        return f"{self.user.username} -> Quiz {self.quiz.id} -> Attempt nr.{self.attempt}"
