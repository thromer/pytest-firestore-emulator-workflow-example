import proto
from _typeshed import Incomplete
from google.protobuf import duration_pb2, timestamp_pb2
from google.type import dayofweek_pb2

__protobuf__: Incomplete

class BackupSchedule(proto.Message):
    name: str
    create_time: timestamp_pb2.Timestamp
    update_time: timestamp_pb2.Timestamp
    retention: duration_pb2.Duration
    daily_recurrence: DailyRecurrence
    weekly_recurrence: WeeklyRecurrence

class DailyRecurrence(proto.Message): ...

class WeeklyRecurrence(proto.Message):
    day: dayofweek_pb2.DayOfWeek
