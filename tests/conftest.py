# pylint: disable=missing-docstring
import errno
import os
import signal
import socket
import subprocess
import sys
import threading
import time
from datetime import datetime
from typing import Generator, Union
import requests
from google.cloud import firestore
import pytest


EMULATOR_HOSTNAME = "localhost"
EMULATOR_PORT = 8080
EMULATOR_HOST = f"{EMULATOR_HOSTNAME}:{EMULATOR_PORT}"
EMULATOR_PROJECT_ID = "firestore-emulator"


def lstr(line: str) -> str:
    return f"{datetime.now().isoformat()} {line}"


def lprint(line: str) -> None:
    print(lstr(line), file=sys.stderr)


def emulator_port_in_use() -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((EMULATOR_HOSTNAME, EMULATOR_PORT))
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            return True
        raise e
    s.close()
    return False


def probe_emulator() -> bool:
    fs = firestore.Client(project=EMULATOR_PROJECT_ID)
    c = fs.collection("c")
    d = c.document("k")
    e: Union[Exception, None] = None
    success = False
    try:
        lprint("probe delete")
        d.delete(timeout=1)
        lprint("probe get")
        d.get(timeout=1)
        lprint("probe succeeded")
        return True
    except Exception as e:
        lprint(f"probe failed {e}")
        return False


def poll_emulator(timeout: int) -> bool:
    """Return True iff the emulator is available within timeout seconds."""
    lprint("enter poll_emulator")
    lprint("Deep health check of emulator")
    start = time.time()
    success = False
    while time.time() - start <= timeout:
        lprint("polling loop")
        if probe_emulator():
            success = True
            break
        time.sleep(1)  # TODO 0.1
    if not success:
        lprint("poll_emulator failed")
        return False
    lprint("poll_emulator done!")
    return True


def start_emulator() -> subprocess.Popen[bytes]:
    lprint("Starting Firestore Emulator")
    start = time.time()
    with subprocess.Popen(
        [
            "firebase",
            "emulators:start",
            "--only",
            "firestore",
        ]
    ) as process:
        lprint(f"started emulator {process.pid=} supposedly ...")

        def monitor_process(stop: threading.Event) -> None:
            lprint("Monitor thread polling ...")
            while True:
                if stop.is_set():
                    lprint("Monitor thread stopped")
                    return
                if process.returncode is not None:
                    if process.returncode:
                        lprint(
                            f"Monitor thread: emulator exited with {process.returncode}"
                        )
                        os.kill(os.getpid(), signal.SIGTERM)
                    else:
                        lprint("Monitor thread: emulator exited happily")
                        return
                time.sleep(0.1)

        monitor_stop = threading.Event()
        monitor_thread = threading.Thread(
            target=monitor_process, args=(monitor_stop,), daemon=True
        )
        monitor_thread.start()
        started = poll_emulator(
            30
        )  # TODO configurable, longer in github action context
        end = time.time()
        lprint(f"Started (?) Firestore Emulator in {end-start} seconds.")
        if not started:
            lprint("Firestore emulator didn't start")
            process.terminate()
            process.wait()
        lprint(f"{process.returncode=}")
        if process.returncode:
            raise RuntimeError(
                lstr(f"Main thread: emulator exited with {process.returncode}")
            )
        lprint("Main stopping monitor")
        monitor_stop.set()
        lprint("monitor_thread.join")
        monitor_thread.join()
        lprint("monitor_thread.joined")
        return process
        # TODO this is a bad way to do it since we're in a with block ...


@pytest.fixture(scope="session", autouse=True)
def start_firestore_emulator(
    request: pytest.FixtureRequest,
) -> Generator[None, None, None]:
    """
    Start the Firestore Emulator if needed.
    """
    # Skip if no tests are marked `firestore`
    if not any(item for item in request.session.items if "firestore" in item.keywords):
        lprint("No tests need Firestore Emulator")
        yield  # Skip starting the emulator
        return  # Presumably needed to avoid teardown

    os.environ["FIRESTORE_EMULATOR_HOST"] = EMULATOR_HOST

    external_emulator = emulator_port_in_use() and probe_emulator()
    if external_emulator:
        lprint("Existing external emulator is already running, reusing it.")
        poll_emulator(30)  # TODO configurable, longer in github action context!
    else:
        process = start_emulator()

    lprint("Let's go test!")
    yield

    if not external_emulator:
        lprint("Stopping Firestore emulator")
        process.terminate()
        process.wait()
        lprint("Stopped Firestore emulator")
        lprint(f"{process.returncode=}")


@pytest.fixture(scope="session")
def firestore_client() -> Generator[firestore.Client, None, None]:
    start = time.time()
    yield firestore.Client(project=EMULATOR_PROJECT_ID)
    end = time.time()
    lprint(f"created client in {end-start} seconds")


@pytest.fixture(scope="function", autouse=True)
def clear_firestore_emulator(request: pytest.FixtureRequest) -> None:
    """
    Clear Firestore Emulator state before each test, if `firestore` is marked.
    """
    if "firestore" in request.keywords:
        lprint("Clearing Firestore Emulator")
        response = requests.delete(
            f"http://{EMULATOR_HOST}/emulator"
            f"/v1/projects/{EMULATOR_PROJECT_ID}/databases/(default)/documents",
            timeout=10,
        )
        response.raise_for_status()
