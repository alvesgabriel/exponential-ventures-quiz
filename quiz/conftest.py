import pytest
from model_bakery import baker

from quiz.quizzes import models


@pytest.fixture
def logged_user(db, django_user_model):
    return baker.make(django_user_model)


@pytest.fixture
def client_logged_user(client, logged_user):
    client.force_login(logged_user)
    return client


@pytest.fixture
def quiz(db):
    return baker.make(models.Quiz)


@pytest.fixture
def questions(quiz):
    return baker.make(models.Question, _quantity=10, quiz=quiz)
