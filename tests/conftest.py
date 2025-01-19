# pylint: disable=missing-docstring
import os
import socket
import sys
import time
from datetime import datetime
from typing import Union, cast
import requests
from google.api_core.exceptions import GoogleAPIError
from google.cloud import firestore
import pytest


EMULATOR_PROJECT_ID = "firestore-emulator"

EMULATOR_HOST_VAR = "FIRESTORE_EMULATOR_HOST"


def lstr(line: str) -> str:
    return f"{datetime.now().isoformat()} {line}"


def probe_emulator_socket() -> bool:
    (host, port_str) = cast(str, os.environ.get(EMULATOR_HOST_VAR)).split(":", 1)
    port = int(port_str)
    try:
        s = socket.create_connection((host, port), timeout=5.0)
        s.close()
    except ConnectionError as e:
        print(f"Unable to connect to {host}:{port}: {e}", file=sys.stderr)
        return False
    return True


def probe_emulator() -> bool:
    if not probe_emulator_socket():
        return False
    fs = firestore.Client(project=EMULATOR_PROJECT_ID)
    c = fs.collection("c")
    d = c.document("k")
    e: Union[Exception, None] = None
    try:
        print("probe get", file=sys.stderr)
        d.get(timeout=5)
        print("probe succeeded", file=sys.stderr)
        return True
    except GoogleAPIError as e:
        print(f"probe failed {e} {type(e)}", file=sys.stderr)
        return False


def assert_firestore_emulator() -> None:
    if not os.environ.get(EMULATOR_HOST_VAR):
        pytest.fail(f"{EMULATOR_HOST_VAR} environment variable not set")
    if not probe_emulator():
        pytest.fail("Firestore Emulator unresponsive")


@pytest.fixture(scope="session")
def firestore_client() -> firestore.Client:
    assert_firestore_emulator()
    start = time.time()
    fs = firestore.Client(project=EMULATOR_PROJECT_ID)
    end = time.time()
    print(f"Created client {fs} in {end-start} seconds", file=sys.stderr)
    return fs


@pytest.fixture(scope="function", autouse=True)
def clear_firestore_emulator(request: pytest.FixtureRequest) -> None:
    """
    Clear Firestore Emulator state before each test using firestore_client fixture.
    """
    # help(request)
    if "firestore_client" in request.fixturenames:
        print("Clearing Firestore Emulator", file=sys.stderr)
        response = requests.delete(
            f"http://{os.environ[f'{EMULATOR_HOST_VAR}']}/emulator"
            f"/v1/projects/{EMULATOR_PROJECT_ID}/databases/(default)/documents",
            timeout=10,
        )
        response.raise_for_status()
