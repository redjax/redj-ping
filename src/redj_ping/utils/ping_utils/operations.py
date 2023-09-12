from __future__ import annotations

import platform
import subprocess

from subprocess import PIPE, CompletedProcess

from .classes import PingResults

from loguru import logger as log

host_platform = platform.system().lower()


def ping_host(
    host: str = None,
    ping_count: int = 3,
    wait_time: int = 1,
) -> PingResults:
    """Start a ping on a remote host.

    Args:
    ----
        host (str): IP address or URL to ping
        ping_count (int): Number of pings to run
        wait_time (int): Time to wait between pings
    """
    if not host:
        raise ValueError("Missing host to ping")

    ## Convert ping flags for platform
    num_param: str = "-n" if host_platform == "windows" else "-c"
    wait_param: str = "-w" if host_platform == "windows" else "-W"

    ## Build command to send
    ping_cmd: list = [
        "ping",
        num_param,
        str(ping_count),
        wait_param,
        str(wait_time),
        host,
    ]

    log.debug(f"Pinging [{host}]...")

    ## Run ping command
    proc: CompletedProcess = subprocess.run(
        ping_cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True
    )

    ## Format output
    output = proc.stdout.strip()
    ## 0, 1
    return_code = proc.returncode

    ## Format lines
    lines = output.split("\n")
    log.debug(f"Lines [{len(lines)}]: {lines}")

    ## Check for ping timeout
    for line in lines:
        if "timed out" in line:
            log.debug(f"Found 'request timed out' line. {line}")

    if return_code == 0:
        ## Ping success
        return_obj_dict = {"host": host, "ping_success": True}
        return_obj: PingResults = PingResults(**return_obj_dict)
    else:
        ## Ping fail
        return_obj_dict = {"host": host, "ping_success": False}
        return_obj: PingResults = PingResults(**return_obj_dict)

    return return_obj


def _ping(
    host: str = None,
    ping_count: int = 3,
    wait_time: int = 1,
    retry_on_fail: bool = False,
    retry_count: int | None = None,
) -> PingResults:
    """Start a ping on a remote host.

    Args:
    ----
        host (str): IP address or URL to ping
        ping_count (int): Number of pings to run
        wait_time (int): Time to wait between pings
        retry_on_fail (bool): Whether or not to retry on unsuccessful ping
        retry_count (int): Number of times to retry if pings fail
    """
    ## Get ping results
    _ping: PingResults = ping_host(
        host=host, ping_count=ping_count, wait_time=wait_time
    )

    ## Check ping success
    if not _ping.ping_success:
        if retry_on_fail:
            ## retry_on_fail = True
            while retry_count > 0:
                log.warning(
                    f"Failed pinging {host}. Retrying {retry_count} more times."
                )

                ## Retry ping
                ping_host(
                    host=host,
                    ping_count=ping_count,
                    wait_time=wait_time,
                )

                retry_count -= 1
        else:
            ## retry_on_fail = False, return results immediately
            _ping.retries = retry_count

            log.debug(f"Ping results: {_ping}")

            return _ping

    else:
        log.debug(f"Ping results: {_ping}")

        return _ping
