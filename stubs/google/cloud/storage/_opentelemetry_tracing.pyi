from _typeshed import Incomplete
from collections.abc import Generator

ENABLE_OTEL_TRACES_ENV_VAR: str
enable_otel_traces: Incomplete
logger: Incomplete
HAS_OPENTELEMETRY: bool

def create_trace_span(name, attributes: Incomplete | None = None, client: Incomplete | None = None, api_request: Incomplete | None = None, retry: Incomplete | None = None) -> Generator[Incomplete]: ...
