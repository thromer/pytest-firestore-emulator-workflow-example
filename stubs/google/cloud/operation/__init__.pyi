from _typeshed import Incomplete

def register_type(klass, type_url: Incomplete | None = None) -> None: ...

class Operation:
    target: Incomplete
    response: Incomplete
    error: Incomplete
    metadata: Incomplete
    name: Incomplete
    client: Incomplete
    caller_metadata: Incomplete
    def __init__(self, name, client, **caller_metadata) -> None: ...
    @classmethod
    def from_pb(cls, operation_pb, client, **caller_metadata): ...
    @classmethod
    def from_dict(cls, operation, client, **caller_metadata): ...
    @property
    def complete(self): ...
    def poll(self): ...
