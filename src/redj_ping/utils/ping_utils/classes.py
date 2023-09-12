from __future__ import annotations

from dataclasses import dataclass, field

@dataclass
class PingResultsBase:
    host: str = field(default=None)
    ping_success: bool = field(default=False)
    retries: int | None = field(default=0)


@dataclass
class PingResults(PingResultsBase):
    pass
