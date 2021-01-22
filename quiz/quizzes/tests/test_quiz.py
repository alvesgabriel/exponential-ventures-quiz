from django.urls import reverse
from rest_framework.status import HTTP_401_UNAUTHORIZED


def test_get_quizzes(resp_quiz):
    quiz = resp_quiz.json()
    assert quiz.get('count') == 1


def test_get_quizes_not_logged(client):
    resp = client.get(reverse('quizzes-list'))
    assert resp.status_code == HTTP_401_UNAUTHORIZED
