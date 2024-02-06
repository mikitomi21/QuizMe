import factory

from .models import Quiz, Question
from users.factories import UserFactory
from .fields import TypeField


class QuizFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quiz

    title = factory.Sequence(lambda n: f"Quiz test {n}")
    description = factory.Sequence(lambda n: f"Description test {n}")
    author = factory.SubFactory(UserFactory)


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    quiz = factory.SubFactory(QuizFactory)
    text = factory.Sequence(lambda n: f"Text test {n}")
    question_type = factory.Iterator(TypeField.OPTIONS[0])
