from circularbuffer import CircularBuffer
import unittest


class CircularBufferTest(unittest.TestCase):

    def test_init(self):
        c = CircularBuffer(3)
        assert c.max_size == 3
        assert c.size == 0
        assert c.start == 0
        assert c.end == 0
        assert c.is_empty() is True
        assert c.is_full() is False

    def test_is_empty(self):
        c = CircularBuffer(3)
        assert c.is_empty() is True
        c.enqueue('A')
        assert c.is_empty() is False
        c.dequeue()
        assert c.is_empty() is True

    def test_is_full(self):
        c = CircularBuffer(3)
        assert c.is_full() is False
        c.enqueue('A')
        assert c.is_full() is False
        c.enqueue('B')
        assert c.is_full() is False
        c.enqueue('C')
        assert c.is_full() is True
        c.dequeue()
        assert c.is_full() is False

    def test_enqueue(self):
        c = CircularBuffer(3)
        c.enqueue('A')
        assert c.size == 1
        assert c.start == 0
        assert c.end == 1
        assert c.front() == 'A'
        c.enqueue('B')
        assert c.size == 2
        assert c.start == 0
        assert c.end == 2
        assert c.front() == 'A'
        c.enqueue('C')
        assert c.size == 3
        assert c.start == 0
        assert c.end == 0
        assert c.front() == 'A'
        assert c.is_full() is True
        with self.assertRaises(ValueError):
            c.enqueue('D')

    def test_front(self):
        c = CircularBuffer(3)
        assert c.front() is None
        c.enqueue('A')
        assert c.front() == 'A'
        c.enqueue('B')
        assert c.front() == 'A'
        c.dequeue()
        assert c.front() == 'B'
        c.dequeue()
        assert c.front() is None
        c.enqueue('C')
        assert c.front() == 'C'

    def test_dequeue(self):
        c = CircularBuffer(3)
        with self.assertRaises(ValueError):
            c.dequeue()
        c.enqueue('A')
        c.enqueue('B')
        c.enqueue('C')
        assert c.dequeue() == 'A'
        c.enqueue('D')
        assert c.dequeue() == 'B'
        assert c.dequeue() == 'C'
        c.enqueue('E')
        c.enqueue('F')
        assert c.dequeue() == 'D'
        assert c.dequeue() == 'E'
        assert c.dequeue() == 'F'
        with self.assertRaises(ValueError):
            c.dequeue()
