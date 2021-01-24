from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    ANSWER_CHOICES = [
        (1, "answer1"),
        (2, "answer2"),
        (3, "answer3"),
        (4, "answer4"),
    ]
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    asking = models.TextField()
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    answer4 = models.CharField(max_length=255)
    right_answer = models.IntegerField(choices=ANSWER_CHOICES)
    order = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("order",)
