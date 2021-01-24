from django.db import models
from quiz.base.models import User
from quiz.quizzes.models import Question, Quiz


class QuizAnswer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    ANSWER_CHOICES = [
        (1, "answer1"),
        (2, "answer2"),
        (3, "answer3"),
        (4, "answer4"),
    ]
    quiz_answer = models.ForeignKey(QuizAnswer, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    select_answer = models.IntegerField(choices=ANSWER_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
