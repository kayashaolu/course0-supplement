#!/usr/bin/env python3
# Demo CLI: enqueues nine jobs and drains them with a Worker. Every third
# job is written to fail, so a fresh clone immediately shows you both the
# success path and the (currently unhandled) failure path -- run
# `python3 -m src.cli` before you touch anything.
#
# Don't run this file directly (`python3 src/cli.py`, or `cd src && python3
# cli.py`) -- either puts `src/` on sys.path and lets this package's own
# queue.py shadow the stdlib's `queue` module, the exact scenario the
# warning at the top of queue.py names. The guard below catches the mistake
# and says so, instead of letting the ModuleNotFoundError below it speak
# first.
if __package__ in (None, ""):
    import sys
    sys.exit(
        "Run this as a module from the repo root (the directory that contains src/) instead: python3 -m src.cli\n"
        "(running it directly puts src/ on sys.path and lets src/queue.py shadow the "
        "stdlib's own queue module -- see the warning at the top of src/queue.py)"
    )

from src.queue import Queue
from src.worker import Worker


def demo_process(job):
    if job["id"] % 3 == 0:
        raise RuntimeError(f"job {job['id']} failed")
    return f"job {job['id']} done"


def main():
    queue = Queue()
    for job_id in range(1, 10):
        queue.enqueue({"id": job_id})

    worker = Worker(queue, demo_process)
    result = worker.drain()
    succeeded = result["succeeded"]
    failed = result["failed"]

    print(f"succeeded: {len(succeeded)}")
    for entry in succeeded:
        print(f"  #{entry['job']['id']}: {entry['result']}")
    print(f"failed: {len(failed)}")
    for entry in failed:
        print(f"  #{entry['job']['id']}: {entry['error']}")


if __name__ == "__main__":
    main()
