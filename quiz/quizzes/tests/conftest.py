import pytest
from django.urls import reverse


@pytest.fixture
def resp_quiz(client_logged_user, quiz):
    return client_logged_user.get(reverse('quizzes-list'))
