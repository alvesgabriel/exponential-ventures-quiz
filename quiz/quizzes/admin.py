from django.contrib import admin
from nested_admin import nested
from quiz.quizzes.models import Question, Quiz


class QuestionInline(nested.NestedStackedInline):
    model = Question
    sortable_by = "order"
    fieldsets = (
        ("Question", {"fields": ("asking",)}),
        ("Answers", {"fields": ("answer1", "answer2", "answer3", "answer4", "right_answer")}),
        (None, {"fields": ("order",)}),
    )


@admin.register(Quiz)
class QuizAdmin(nested.NestedModelAdmin):
    inlines = (QuestionInline,)
    list_display = ("id", "name", "created")
