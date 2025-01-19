# pylint: disable=missing-docstring

from google.cloud import firestore


def test_firestore_2a(firestore_client: firestore.Client) -> None:
    print("test_firestore_2a")


def test_firestore_2b(firestore_client: firestore.Client) -> None:
    print("test_firestore_2b")
