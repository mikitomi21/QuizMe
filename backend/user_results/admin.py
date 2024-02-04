from django.contrib import admin

from .models import PlayerResultOfQuiz


# Register your models here.


@admin.register(PlayerResultOfQuiz)
class AdminResult(admin.ModelAdmin):
    list_display = ["user", "quiz", "attempt", "correct_answers", "wrong_answers"]
