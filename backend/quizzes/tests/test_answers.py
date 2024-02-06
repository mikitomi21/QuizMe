from rest_framework.test import APITestCase
from django.db import transaction

from quizzes.models import Answer
from quizzes.factories import QuestionFactory


class TestAnswer(APITestCase):
    def setUp(self):
        self.text = "text test"
        self.is_correct = True
        self.question = QuestionFactory()

    def tearDown(self):
        Answer.objects.filter(text=self.text, is_correct=self.is_correct, question=self.question).delete()

    def test_create_answer(self):
        answer = Answer.objects.create(
            text=self.text,
            is_correct=self.is_correct,
            question=self.question,
        )

        self.assertEqual(answer.text, self.text)
        self.assertEqual(answer.is_correct, self.is_correct)
        self.assertEqual(answer.question, self.question)

    def test_create_answer_without_question(self):
        with transaction.atomic():
            with self.assertRaises(Exception):
                Answer.objects.create(text=self.text, is_correct=self.is_correct)
