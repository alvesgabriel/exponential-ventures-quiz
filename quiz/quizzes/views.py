from quiz.quizzes.models import Quiz
from quiz.quizzes.serializers import QuizSerializer
from rest_framework import permissions, viewsets


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all().order_by("created")
    serializer_class = QuizSerializer
    allowed_methods = ("GET",)
    permission_classes = (permissions.IsAuthenticated,)
