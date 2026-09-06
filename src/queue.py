# A minimal in-memory FIFO job queue.
#
# The queue does not interpret jobs -- a job is any value the caller
# enqueues (a dict, a string, whatever process() expects). This is the
# "Queue" building block: storage that holds work waiting to be done.
#
# Gotcha worth a comment: this module is named queue.py, which shadows the
# stdlib queue module by name. It is never actually shadowed in practice --
# this file is only ever imported as src.queue (a submodule of the src
# package), and the CLI is run as `python3 -m src.cli` from the repo root
# (the directory that contains `src/`),
# so the stdlib's own `import queue` (used internally by some stdlib
# modules) keeps resolving to the real stdlib module, not this one. Still,
# don't `cd src && python3 queue.py` or run anything that puts this
# directory directly on sys.path -- that's the scenario where the shadow
# would actually bite.


class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, job):
        if job is None:
            raise TypeError("Queue.enqueue requires a job (got None)")
        self._items.append(job)

    def dequeue(self):
        if not self._items:
            return None
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0
