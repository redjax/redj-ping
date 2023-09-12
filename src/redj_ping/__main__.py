from __future__ import annotations

import stackprinter

stackprinter.set_excepthook(style="darkbg2")

from constants import (
    PING_COUNT,
    PING_HOST,
    PING_RETRY,
    PING_RETRY_COUNT,
    PING_WAIT,
    PING_RETRY_TIMEOUT,
    env_string,
)
from loguru import logger as log
from utils.loguru_utils import init_logger
from utils.ping_utils import PingResults, _ping

from domain.ping import PingTarget

init_logger


def ping(target: PingTarget = None):
    ping_results: PingResults = _ping(target=target)
    log.debug(f"Ping results: {ping_results}")

    return ping_results


if __name__ == "__main__":
    tar = PingTarget(
        host=PING_HOST,
        count=PING_COUNT,
        wait=PING_WAIT,
        retry=PING_RETRY,
        retry_count=PING_RETRY_COUNT,
        retry_timeout=PING_RETRY_TIMEOUT,
    )

    results = ping(target=tar)
