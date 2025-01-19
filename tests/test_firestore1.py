# pylint: disable=missing-docstring

from google.cloud import firestore

import pytest


@pytest.mark.firestore
def test_firestore_1a(firestore_client: firestore.Client) -> None:
    print(f"{firestore_client=}")
    print("test_firestore_1a")
    c = firestore_client.collection("c")
    d = c.document("k")
    d.set({"k": "v"})
    print(d.get().to_dict())


@pytest.mark.firestore
def test_firestore_1b(firestore_client: firestore.Client) -> None:
    print(f"{firestore_client=}")
    print("test_firestore_1b")
