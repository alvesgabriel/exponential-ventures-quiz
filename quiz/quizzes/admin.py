from django.contrib import admin
from quiz.quizzes.models import Quiz


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created")
