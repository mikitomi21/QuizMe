from rest_framework.test import APITestCase
from quizzes.models import Quiz
from users.factories import UserFactory


class TestQuizzes(APITestCase):
    def setUp(self):
        self.title = "title test"
        self.description = "title description"
        self.author = UserFactory()

    def tearDown(self):
        Quiz.objects.filter(title=self.title, description=self.description, author=self.author).delete()

    def test_create_quiz(self):
        quiz = Quiz.objects.create(
            title=self.title,
            description=self.description,
            author=self.author,
        )

        self.assertEqual(quiz.title, self.title)
        self.assertEqual(quiz.description, self.description)
        self.assertEqual(quiz.author, self.author)
