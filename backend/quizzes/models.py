from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    # author =
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:30]


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.quiz.title[:30]} > {self.text[:30]}"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return f"True: {self.text[:30]}" if self.is_correct else f"False: {self.text[:30]}"
