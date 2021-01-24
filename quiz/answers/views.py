from quiz.answers.models import QuizAnswer
from quiz.answers.serializers import QuizAnswerSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response


class QuizAnswerViewSet(generics.ListCreateAPIView):
    serializer_class = QuizAnswerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return QuizAnswer.objects.filter(user=self.request.user.id)

    def get_serializer_context(self):
        return {
            **super().get_serializer_context(),
            "user": self.request.user,
            "quiz_id": self.kwargs.get("quiz_pk")
        }

    def post(self, request, *args, **kwargs):
        print(type(request.data))
        print(request.data)
        serializer = self.get_serializer(data={
            **request.data,
            "quiz": kwargs.get("quiz_pk"),
            "user": request.user.id,
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
