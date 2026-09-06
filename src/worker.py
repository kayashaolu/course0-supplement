# A Worker drains a Queue by calling process(job) for each job in turn.
# This is the "Worker" building block: a task runner that pulls from
# storage instead of waiting to be called directly, like a Service does.
#
# BASELINE BEHAVIOR (intentional, and what Task 1 replaces): if
# process(job) raises, the job is recorded as failed and dropped. There is
# no retry, no backoff, and no record kept beyond the summary that drain()
# returns. A failed job is gone once drain() returns -- nothing in this
# file remembers it happened.


class Worker:
    def __init__(self, queue, process):
        if not callable(process):
            raise TypeError("Worker requires a process(job) callable")
        self._queue = queue
        self._process = process

    def drain(self):
        """Runs every job currently in the queue to completion or failure.

        Re-checks is_empty() on each loop, rather than snapshotting the
        size up front.

        Returns a dict with "succeeded" and "failed" keys, each a list of
        {"job": ..., "result": ...} / {"job": ..., "error": ...} records in
        the order processed.

        Stays a plain def, not an async def: an async drain() would force
        every caller to await it, and nothing about draining an in-memory
        queue needs that here.
        """
        succeeded = []
        failed = []
        while not self._queue.is_empty():
            job = self._queue.dequeue()
            try:
                result = self._process(job)
                succeeded.append({"job": job, "result": result})
            except Exception as error:
                failed.append({"job": job, "error": error})
        return {"succeeded": succeeded, "failed": failed}
