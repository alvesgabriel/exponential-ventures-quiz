import pytest
from django.urls import reverse
from model_bakery import baker
from quiz.quizzes import models
from rest_framework.status import HTTP_401_UNAUTHORIZED


@pytest.fixture
def questions(quiz):
    return baker.make(models.Question, _quantity=10, quiz=quiz)


@pytest.fixture
def resp_question(client_logged_user, quiz, questions):
    return client_logged_user.get(reverse('questions-list', kwargs={'quiz_pk': quiz.id}))


def test_get_questions(resp_question):
    questions = resp_question.json()
    assert questions.get('count') == 10


def test_get_question_not_logged(client):
    resp = client.get(reverse('questions-list', kwargs={'quiz_pk': 0}))
    assert resp.status_code == HTTP_401_UNAUTHORIZED
