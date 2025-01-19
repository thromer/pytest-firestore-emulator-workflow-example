from _typeshed import Incomplete
from google.cloud.firestore_bundle.types.bundle import BundledDocumentMetadata
from google.cloud.firestore_v1.base_client import BaseClient as BaseClient
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.base_query import BaseQuery

class FirestoreBundle:
    BUNDLE_SCHEMA_VERSION: int
    name: Incomplete
    documents: Incomplete
    named_queries: Incomplete
    latest_read_time: Incomplete
    def __init__(self, name: str) -> None: ...
    def add_document(self, snapshot: DocumentSnapshot) -> FirestoreBundle: ...
    def add_named_query(self, name: str, query: BaseQuery) -> FirestoreBundle: ...
    def build(self) -> str: ...

class _BundledDocument:
    snapshot: Incomplete
    metadata: Incomplete
    def __init__(self, snapshot: DocumentSnapshot, metadata: BundledDocumentMetadata) -> None: ...
