import pytest
from django.urls import reverse
from model_bakery import baker
from quiz.quizzes import models


@pytest.fixture
def quiz(db):
    return baker.make(models.Quiz)


@pytest.fixture
def resp_quiz(client_logged_user, quiz):
    return client_logged_user.get(reverse('quizzes-list'))
