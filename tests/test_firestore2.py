# pylint: disable=missing-docstring

import pytest


pytestmark = pytest.mark.firestore


@pytest.mark.firestore
def test_firestore_2a() -> None:
    print("test_firestore_2a")


def test_firestore_2b() -> None:
    print("test_firestore_2b")
