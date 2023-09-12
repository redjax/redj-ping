from __future__ import annotations

import stackprinter

stackprinter.set_excepthook(style="darkbg2")

from constants import (
    PING_COUNT,
    PING_HOST,
    PING_RETRY,
    PING_RETRY_COUNT,
    PING_RETRY_TIMEOUT,
    PING_WAIT,
    env_string,
)

# from utils.ping_utils import PingResults, _ping
from domain.ping import PingResults, PingTarget
from loguru import logger as log
from utils.loguru_utils import init_logger

if __name__ == "__main__":
    init_logger

    tar = PingTarget(
        host=PING_HOST,
        count=PING_COUNT,
        wait=PING_WAIT,
        retry=PING_RETRY,
        retry_count=PING_RETRY_COUNT,
        retry_timeout=PING_RETRY_TIMEOUT,
    )

    results = tar.ping()
    log.info(f"Results: {results}")
