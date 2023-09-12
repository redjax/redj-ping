from dataclasses import dataclass, field


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
        if self.retry_count is not None:
            assert isinstance(self.retry_count, int)
            assert self.retry_count > 0
        if self.retry_timeout is not None:
            assert isinstance(self.retry_timeout, int)
            assert self.retry_count > 0


@dataclass
class PingTarget(PingTargetBase):
    pass


@dataclass
class PingResultsBase:
    host: str = field(default=None)
    ping_success: bool = field(default=False)
    retries: int | None = field(default=0)


@dataclass
class PingResults(PingResultsBase):
    pass
