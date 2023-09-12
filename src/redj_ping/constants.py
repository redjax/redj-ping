from __future__ import annotations

from dynaconf import settings

ENV: str = settings.ENV or "prod"
CONTAINER_ENV: bool = settings.CONTAINER_ENV or False
LOG_LEVEL: str = settings.LOG_LEVEL or "INFO"
PING_HOST: str = settings.PING_HOST or "www.google.com"
PING_COUNT: int = settings.PING_COUNT or 3
PING_WAIT: int = settings.PING_WAIT or 1
PING_RETRY: bool = settings.PING_RETRY or False
PING_RETRY_COUNT: int = settings.PING_RETRY_COUNT or 0
PING_RETRY_TIMEOUT: int = settings.PING_RETRY_TIMEOUT or 5

env_string: str = f"[env:{ENV}|container:{CONTAINER_ENV}]"
