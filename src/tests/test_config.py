import pytest


@pytest.mark.config
def test_app_env(app_env):
    assert app_env is not None
    assert app_env in ["dev", "prod"]


@pytest.mark.config
def test_ping_host(ping_host):
    assert ping_host is not None
    assert isinstance(ping_host, str)


@pytest.mark.config
def test_ping_count(ping_count):
    assert ping_count is not None
    assert isinstance(ping_count, int)
    assert ping_count > 0 and ping_count < 255


@pytest.mark.config
def test_ping_wait(ping_wait):
    assert ping_wait is not None
    assert isinstance(ping_wait, int)
    assert ping_wait > 0


@pytest.mark.config
def test_ping_retry(ping_retry):
    assert ping_retry is not None
    assert isinstance(ping_retry, bool)


@pytest.mark.config
def test_ping_retry_count(ping_retry, ping_retry_count):
    if ping_retry:
        assert ping_retry_count is not None
        assert isinstance(ping_retry_count, int)
        assert ping_retry_count > 0
