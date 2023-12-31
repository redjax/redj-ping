from __future__ import annotations

from dataclasses import dataclass, field
import platform
import subprocess

from subprocess import PIPE, CompletedProcess

from loguru import logger as log

host_platform = platform.system().lower()


def ping_host(target: "PingTarget" = None):
    if not target.host:
        raise ValueError("Missing host to ping")

    ## Convert ping flags for platform
    num_param: str = "-n" if host_platform == "windows" else "-c"
    wait_param: str = "-w" if host_platform == "windows" else "-W"

    ## Build command to send
    ping_cmd: list = [
        "ping",
        num_param,
        str(target.count),
        wait_param,
        str(target.wait),
        target.host,
    ]

    log.debug(f"Pinging [{target.host}]...")

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
        return_obj_dict = {"host": target.host, "ping_success": True}
        return_obj: PingResults = PingResults(**return_obj_dict)
    else:
        ## Ping fail
        return_obj_dict = {"host": target.host, "ping_success": False}
        return_obj: PingResults = PingResults(**return_obj_dict)

    return return_obj


def _ping(target: "PingTarget" = None):
    assert target is not None, "Must pass a PingTarget class instance."
    assert isinstance(target, PingTarget), "Target must be an instance of PingTarget"

    _ping: PingResults = ping_host(target=target)

    ## Check ping success
    if not _ping.ping_success:
        if target.retry:
            if target.retry_timeout is None or 0:
                target.retry_timeout = 5

            ## retry_on_fail = True
            while target.retry_count > 0:
                log.warning(
                    f"Failed pinging {target.host}. Waiting {target.retry_timeout} seconds, then retrying {target.retry_count} more times."
                )

                ## Retry ping
                _ping: PingResults = ping_host(target=target)

                if _ping.ping_success:
                    return _ping
                else:
                    if _ping.retries == 0:
                        return _ping
                    else:
                        target.retry_count -= 1

        else:
            ## retry_on_fail = False, return results immediately
            _ping.retries = target.retry_count

            log.debug(f"Ping results: {_ping}")

            return _ping

    else:
        log.debug(f"Ping results: {_ping}")

        return _ping


@dataclass
class PingTargetBase:
    host: str = field(default=None)

    count: int = field(default=3)
    wait: int = field(default=1)
    retry: bool | None = field(default=False)
    retry_count: int | None = field(default=None)
    retry_timeout: int | None = field(default=5)

    def __post_init__(self):
        """Initialize the class by validating inputs."""
        assert self.host is not None, "Must set a host to ping"

        if self.retry_count is not None:
            assert isinstance(self.retry_count, int)
            assert self.retry_count > 0
        if self.retry_timeout is not None:
            assert isinstance(self.retry_timeout, int)
            assert self.retry_count > 0


@dataclass
class PingTarget(PingTargetBase):
    def ping(self):
        results: PingResults = _ping(target=self)

        return results


@dataclass
class PingResultsBase:
    host: str = field(default=None)
    ping_success: bool = field(default=False)
    retries: int | None = field(default=0)


@dataclass
class PingResults(PingResultsBase):
    pass
