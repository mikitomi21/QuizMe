from django.core.management.base import BaseCommand

from users.models import CustomUser
from quizzes.models import Quiz, Question, Answer


class Command(BaseCommand):
    help = "Clear an entire database"

    def handle(self, *args, **options):
        self.stdout.write("Deleting data from database...")
        Question.objects.all().delete()
        Answer.objects.all().delete()
        Quiz.objects.all().delete()
        CustomUser.objects.all().delete()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully Deleted all data from database")
        )
