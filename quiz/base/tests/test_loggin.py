import pytest
from django.urls import reverse
from model_bakery import baker


@pytest.fixture
def user(db, django_user_model):
    user_model = baker.make(django_user_model)
    password = 'password'
    user_model.set_password(password)
    user_model.save()
    user_model.flat_password = password
    return user_model


@pytest.fixture
def login(client, user):
    body = {
        'username': user.email,
        'password': user.flat_password,
    }
    return client.post(reverse('login_token'), body).json()


def test_login(login):
    assert 'token' in login
