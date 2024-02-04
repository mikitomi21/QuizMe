from django.core.management.base import BaseCommand
from quizzes.models import Quiz, Question, Answer
from users.models import CustomUser
from django.contrib.auth import get_user_model
from quizzes.fields import TypeField

from faker import Faker
import random

NUMBER_OF_USERS = 5
NUMBER_OF_QUIZZES = 3
NUMBER_OF_QUESTIONS_PER_QUIZ = 4
NUMBER_OF_ANSWERS_PER_QUESTION = 4
QUESTION_TYPES = ["CLOSED", "OPEN", "MULTIPLE_CHOICE"]

fake = Faker("pl_PL")


class Command(BaseCommand):
    help = "Create default data into database"

    def handle(self, *args, **options):
        self.stdout.write("Start creating default data...")

        self.create_admin()
        self.create_users()
        self.create_quizzes()

        self.stdout.write("Finish creating default data")

    def create_admin(self):
        try:
            User = get_user_model()
            user = User.objects.create_superuser(
                email="admin@gmail.com",
                username="admin",
                password="zaq1@WSX",
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {user.username}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating superuser: {e}'))

    def create_users(self):
        try:
            for _ in range(NUMBER_OF_USERS):
                user = CustomUser(
                    email=fake.email(),
                    username=fake.name(),
                    password=fake.password(),
                )
                user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created users'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating users: {e}'))

    def create_quizzes(self):
        quizzes = []
        try:
            for _ in range(NUMBER_OF_QUIZZES):
                quiz = Quiz(
                    title=fake.sentence(),
                    description=fake.paragraph(),
                    author=random.choice(CustomUser.objects.all())
                )
                quiz.save()
                quizzes.append(quiz)
            self.stdout.write(self.style.SUCCESS(f'Successfully created quizzes'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating quizzes: {e}'))

        self.create_questions(quizzes)

    def create_questions(self, quizzes: list[Quiz]):
        questions = []
        try:
            for quiz in quizzes:
                for _ in range(NUMBER_OF_QUESTIONS_PER_QUIZ):
                    question = Question(
                        quiz=quiz,
                        text=fake.sentence(),
                        question_type=random.choice(QUESTION_TYPES)
                    )
                    question.save()
                    questions.append(question)
            self.stdout.write(self.style.SUCCESS(f'Successfully created questions'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating questions: {e}'))

        self.create_answer(questions)

    def create_answer(self, questions: list[Question]):
        try:
            for question in questions:
                if question.question_type == TypeField.CLOSED:
                    answers: list[Answer] = []
                    for _ in range(NUMBER_OF_ANSWERS_PER_QUESTION):
                        answer = Answer(
                            question=question,
                            text=fake.sentence(),
                            is_correct=False,
                        )
                        answers.append(answer)
                    random.choice(answers).is_correct = True

                    for answer in answers:
                        answer.save()

                elif question.question_type == TypeField.MULTIPLE_CHOICE:
                    for _ in range(NUMBER_OF_ANSWERS_PER_QUESTION):
                        is_correct = random.choice([True, False])
                        answer = Answer(
                            question=question,
                            text=fake.sentence(),
                            is_correct=is_correct,
                        )
                        answer.save()

                elif question.question_type == TypeField.OPEN:
                    continue
            self.stdout.write(self.style.SUCCESS(f'Successfully created answers'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating answers: {e}'))
