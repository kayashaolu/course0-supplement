import unittest

from src.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue_is_fifo(self):
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        self.assertEqual(q.dequeue(), "a")
        self.assertEqual(q.dequeue(), "b")

    def test_is_empty_and_size_reflect_queue_contents(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        self.assertEqual(q.size(), 0)
        q.enqueue(1)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), 1)

    def test_dequeue_on_an_empty_queue_returns_none(self):
        q = Queue()
        self.assertIsNone(q.dequeue())

    def test_enqueue_rejects_none(self):
        q = Queue()
        with self.assertRaises(TypeError):
            q.enqueue(None)


if __name__ == "__main__":
    unittest.main()
