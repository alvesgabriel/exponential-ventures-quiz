import pytest
from model_bakery import baker


@pytest.fixture
def logged_user(db, django_user_model):
    return baker.make(django_user_model)


@pytest.fixture
def client_logged_user(client, logged_user):
    client.force_login(logged_user)
    return client
