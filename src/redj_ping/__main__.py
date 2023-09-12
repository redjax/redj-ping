from __future__ import annotations

import stackprinter

stackprinter.set_excepthook(style="darkbg2")

from constants import (
    PING_COUNT,
    PING_HOST,
    PING_RETRY,
    PING_RETRY_COUNT,
    PING_WAIT,
    env_string,
)
from loguru import logger as log
from utils.loguru_utils import init_logger
from utils.ping_utils import PingResults, _ping

init_logger


def ping(
    host: str = PING_HOST,
    ping_count: int = PING_COUNT,
    wait_time: int = PING_WAIT,
    retry_on_fail: bool = PING_RETRY,
    retry_count: int = PING_RETRY_COUNT,
):
    ping_settings: dict = {
        "host": host,
        "ping_count": ping_count,
        "wait_time": wait_time,
        "retry_on_fail": retry_on_fail,
        "retry_count": retry_count,
    }

    ping_results: PingResults = _ping(**ping_settings)
    log.debug(f"Ping results: {ping_results}")

    return ping_results


if __name__ == "__main__":
    log.info(env_string)

    ping()
