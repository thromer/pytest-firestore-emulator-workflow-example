from enum import Enum
from typing import Any

class TypeOrder(Enum):
    NULL = 0
    BOOLEAN = 1
    NUMBER = 2
    TIMESTAMP = 3
    STRING = 4
    BLOB = 5
    REF = 6
    GEO_POINT = 7
    ARRAY = 8
    OBJECT = 9
    VECTOR = 10
    @staticmethod
    def from_value(value) -> Any: ...

class Order:
    @classmethod
    def compare(cls, left, right) -> int: ...
    @staticmethod
    def compare_blobs(left, right) -> int: ...
    @staticmethod
    def compare_timestamps(left, right) -> Any: ...
    @staticmethod
    def compare_geo_points(left, right) -> Any: ...
    @staticmethod
    def compare_resource_paths(left, right) -> int: ...
    @staticmethod
    def compare_arrays(left, right) -> int: ...
    @staticmethod
    def compare_vectors(left, right) -> int: ...
    @staticmethod
    def compare_objects(left, right) -> int: ...
    @staticmethod
    def compare_numbers(left, right) -> int: ...
    @staticmethod
    def compare_doubles(left, right) -> int: ...
