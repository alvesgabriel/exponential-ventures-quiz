from quiz.quizzes.models import Question, Quiz
from quiz.quizzes.serializers import QuestionSerializer, QuizSerializer
from rest_framework import generics, permissions


class QuizViewSet(generics.ListAPIView):
    queryset = Quiz.objects.all().order_by("created")
    serializer_class = QuizSerializer
    permission_classes = (permissions.IsAuthenticated,)


class QuestionViewSet(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Question.objects.filter(quiz=self.kwargs.get("quiz_pk"))
