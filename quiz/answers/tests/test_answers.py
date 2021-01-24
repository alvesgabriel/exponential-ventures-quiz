import pytest
from django.urls import reverse
from quiz.answers.models import Answer
from rest_framework.status import HTTP_201_CREATED


@pytest.fixture
def answers(questions):
    return [
        Answer(question=question, select_answer=question.answer1)
        # {
        #     "question": question,
        #     "select_answer": question.answer1,
        # }
        for question in questions
    ]


@pytest.fixture
def resp_post_answer(client_logged_user, quiz, answers):
    body = {
        "answers": answers
    }
    return client_logged_user.post(
        reverse('answers-list', kwargs={'quiz_pk': quiz.id}),
        data=body,
    )


@pytest.fixture
def resp_get_answer(client_logged_user, quiz, resp_post_answer):
    return client_logged_user.get(reverse('answers-list', kwargs={'quiz_pk': quiz.id}))


def test_post_status(resp_post_answer):
    assert resp_post_answer.json() == {}
    assert resp_post_answer.status_code == HTTP_201_CREATED


def test_get(resp_get_answer):
    data = resp_get_answer.json()
    assert data.get('count') == 1
