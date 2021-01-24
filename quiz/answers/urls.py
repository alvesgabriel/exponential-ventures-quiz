from django.urls import path
from quiz.answers import views

urlpatterns = [
    path(
        "<int:quiz_pk>/answers/",
        views.QuizAnswerViewSet.as_view(),
        name="answers-list",
    ),
]
