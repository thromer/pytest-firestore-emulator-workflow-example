from _typeshed import Incomplete
from typing import Iterable

PATH_ELEMENT_TOKENS: Incomplete
TOKENS_PATTERN: Incomplete
TOKENS_REGEX: Incomplete

def split_field_path(path: str | None): ...
def parse_field_path(api_repr: str): ...
def render_field_path(field_names: Iterable[str]): ...
get_field_path = render_field_path

def get_nested_value(field_path: str, data: dict): ...

class FieldPath:
    parts: Incomplete
    def __init__(self, *parts) -> None: ...
    @classmethod
    def from_api_repr(cls, api_repr: str): ...
    @classmethod
    def from_string(cls, path_string: str): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __add__(self, other): ...
    def to_api_repr(self): ...
    def eq_or_parent(self, other): ...
    def lineage(self): ...
    @staticmethod
    def document_id(): ...
