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
from utils.ping_utils import PingResults, ping

init_logger

if __name__ == "__main__":
    log.info(env_string)

    ping_settings: dict = {
        "host": PING_HOST,
        "ping_count": PING_COUNT,
        "wait_time": PING_WAIT,
        "retry_on_fail": PING_RETRY,
        "retry_count": PING_RETRY_COUNT,
    }

    _ping: PingResults = ping(**ping_settings)
    log.debug(f"Ping results: {_ping}")
