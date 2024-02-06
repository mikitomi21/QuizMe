from rest_framework.test import APITestCase
from django.db import transaction

from quizzes.models import Question
from quizzes.factories import QuizFactory
from quizzes.fields import TypeField


class TestQuestions(APITestCase):
    def setUp(self):
        self.text = "text test"
        self.question_type = TypeField.CLOSED
        self.quiz = QuizFactory()

    def tearDown(self):
        Question.objects.filter(text=self.text, question_type=self.question_type, quiz=self.quiz).delete()

    def test_create_question(self):
        question = Question.objects.create(
            text=self.text,
            question_type=self.question_type,
            quiz=self.quiz,
        )

        self.assertEqual(question.text, self.text)
        self.assertEqual(question.question_type, self.question_type)
        self.assertEqual(question.quiz, self.quiz)

    def test_create_question_without_quiz(self):
        with transaction.atomic():
            with self.assertRaises(Exception):
                Question.objects.create(
                    text=self.text,
                    question_type=self.question_type,
                )
