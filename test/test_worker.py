import unittest

from src.queue import Queue
from src.worker import Worker


class TestWorker(unittest.TestCase):
    def test_drain_processes_every_job_and_reports_success(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        worker = Worker(q, lambda job: job * 10)
        result = worker.drain()
        succeeded = result["succeeded"]
        failed = result["failed"]
        self.assertEqual(len(succeeded), 2)
        self.assertEqual(len(failed), 0)
        self.assertEqual([s["result"] for s in succeeded], [10, 20])
        self.assertTrue(q.is_empty())

    def test_a_raising_job_is_reported_failed_not_retried(self):
        q = Queue()
        q.enqueue("ok")
        q.enqueue("boom")
        calls = {"count": 0}

        def process(job):
            calls["count"] += 1
            if job == "boom":
                raise RuntimeError("nope")
            return job

        worker = Worker(q, process)
        result = worker.drain()
        succeeded = result["succeeded"]
        failed = result["failed"]
        self.assertEqual(len(succeeded), 1)
        self.assertEqual(len(failed), 1)
        self.assertEqual(failed[0]["job"], "boom")
        # Baseline has no retry: each job is attempted exactly once.
        self.assertEqual(calls["count"], 2)

    def test_constructor_requires_a_process_callable(self):
        q = Queue()
        with self.assertRaises(TypeError):
            Worker(q, None)


if __name__ == "__main__":
    unittest.main()
