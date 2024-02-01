from django.contrib import admin
from .models import Quiz, Question, Answer

# Register your models here.


@admin.register(Quiz)
class AdminQuiz(admin.ModelAdmin):
    list_display = ["title", "created", "updated"]


@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ["quiz", "text"]


@admin.register(Answer)
class AdminQuestion(admin.ModelAdmin):
    list_display = ["question", "text", "is_correct"]