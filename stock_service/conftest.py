import pytest
from django.contrib.auth import get_user_model

from stock_service.api.tests.factories import UserFactory

User = get_user_model()


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def user_creation():
    return UserFactory()
