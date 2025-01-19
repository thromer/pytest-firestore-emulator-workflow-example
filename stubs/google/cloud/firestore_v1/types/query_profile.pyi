import proto
from _typeshed import Incomplete
from google.protobuf import duration_pb2, struct_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class ExplainOptions(proto.Message):
    analyze: bool

class ExplainMetrics(proto.Message):
    plan_summary: PlanSummary
    execution_stats: ExecutionStats

class PlanSummary(proto.Message):
    indexes_used: MutableSequence[struct_pb2.Struct]

class ExecutionStats(proto.Message):
    results_returned: int
    execution_duration: duration_pb2.Duration
    read_operations: int
    debug_stats: struct_pb2.Struct
