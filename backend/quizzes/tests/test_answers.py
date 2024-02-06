from rest_framework.test import APITestCase
from quizzes.models import Answer
from quizzes.factories import QuestionFactory


class TestQuestions(APITestCase):
    def setUp(self):
        self.text = "text test"
        self.is_correct = "True"
        self.question = QuestionFactory()

    def test_create_quiz(self):
        answer = Answer.objects.create(
            text=self.text,
            is_correct=self.is_correct,
            question=self.question,
        )

        self.assertEqual(answer.text, self.text)
        self.assertEqual(answer.is_correct, self.is_correct)
        self.assertEqual(answer.question, self.question)
