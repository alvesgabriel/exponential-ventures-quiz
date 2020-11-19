from quiz.quizzes.models import Question, Quiz
from quiz.quizzes.serializers import QuestionSerializer, QuizSerializer
from rest_framework import permissions, viewsets


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all().order_by("created")
    serializer_class = QuizSerializer
    allowed_methods = ("GET",)
    permission_classes = (permissions.IsAuthenticated,)


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    allowed_methods = ("GET",)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Question.objects.filter(quiz=self.kwargs.get("quiz_pk"))
