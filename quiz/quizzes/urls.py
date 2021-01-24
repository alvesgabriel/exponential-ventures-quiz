from django.urls import path
from quiz.quizzes import views

urlpatterns = [
    path(
        "",
        views.QuizViewSet.as_view(),
        name="quizzes-list",
    ),
    path(
        "<int:quiz_pk>/questions/",
        views.QuestionViewSet.as_view(),
        name="questions-list",
    ),
]
