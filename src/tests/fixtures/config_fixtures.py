import pytest

## Import settings for testing
from dynaconf import settings


@pytest.fixture
def app_env():
    env = settings.ENV

    return env


@pytest.fixture
def ping_host():
    host = settings.PING_HOST

    return host


@pytest.fixture
def ping_count():
    count = settings.PING_COUNT

    return count


@pytest.fixture
def ping_wait():
    wait = settings.PING_WAIT

    return wait


@pytest.fixture
def ping_retry():
    retry = settings.PING_RETRY

    return retry


@pytest.fixture
def ping_retry_count():
    retry_count = settings.PING_RETRY_COUNT

    return retry_count
