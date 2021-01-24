from quiz.quizzes.models import Question, Quiz
from rest_framework import serializers


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer()

    class Meta:
        model = Question
        fields = (
            'quiz',
            'asking',
            'answer1',
            'answer2',
            'answer3',
            'answer4',
            'order',
        )
