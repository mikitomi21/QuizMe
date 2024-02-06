import factory
from .models import Quiz, Question


class QuizFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quiz

    # TODO dokonczyc


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    # TODO dokonczyc
