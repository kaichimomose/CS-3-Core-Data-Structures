#!python

from deque import Deque
import unittest


class DequeTest(unittest.TestCase):

    def test_init(self):
        d = Deque()
        assert d.front() is None
        assert d.back() is None
        assert d.is_empty() is True
        assert d.length() == 0

    def test_init_with_list(self):
        d = Deque(['A', 'B', 'C'])
        assert d.front() == 'A'
        assert d.back() == 'C'
        assert d.is_empty() is False
        assert d.length() == 3

    def test_length(self):
        d = Deque()
        assert d.length() == 0
        assert d.is_empty() is True
        d.push_front('A')
        assert d.length() == 1
        assert d.is_empty() is False
        d.push_back('B')
        assert d.length() == 2
        assert d.is_empty() is False
        d.pop_front()
        assert d.length() == 1
        assert d.is_empty() is False
        d.pop_back()
        assert d.length() == 0
        assert d.is_empty() is True

    def test_push_front(self):
        d = Deque()
        d.push_front('A')
        assert d.front() == 'A'
        assert d.back() == 'A'
        assert d.length() == 1
        d.push_front('B')
        assert d.front() == 'B'
        assert d.back() == 'A'
        assert d.length() == 2
        d.push_front('C')
        assert d.front() == 'C'
        assert d.back() == 'A'
        assert d.length() == 3
        assert d.is_empty() is False

    def test_push_back(self):
        d = Deque()
        d.push_back('A')
        assert d.front() == 'A'
        assert d.back() == 'A'
        assert d.length() == 1
        d.push_back('B')
        assert d.front() == 'A'
        assert d.back() == 'B'
        assert d.length() == 2
        d.push_back('C')
        assert d.front() == 'A'
        assert d.back() == 'C'
        assert d.length() == 3
        assert d.is_empty() is False

    def test_front(self):
        d = Deque()
        assert d.front() is None
        d.push_front('A')
        assert d.front() == 'A'
        d.push_back('B')
        assert d.front() == 'A'
        d.push_front('C')
        assert d.front() == 'C'
        d.pop_front()
        assert d.front() == 'A'
        d.pop_front()
        assert d.front() == 'B'
        d.pop_back()
        assert d.front() is None

    def test_back(self):
        d = Deque()
        assert d.back() is None
        d.push_front('A')
        assert d.back() == 'A'
        d.push_back('B')
        assert d.back() == 'B'
        d.push_front('C')
        assert d.back() == 'B'
        d.pop_back()
        assert d.back() == 'A'
        d.pop_back()
        assert d.back() == 'C'
        d.pop_front()
        assert d.back() is None

    def test_pop_front(self):
        d = Deque(['A', 'B', 'C'])
        assert d.pop_front() == 'A'
        assert d.length() == 2
        assert d.pop_front() == 'B'
        assert d.length() == 1
        assert d.pop_front() == 'C'
        assert d.length() == 0
        assert d.is_empty() is True
        with self.assertRaises(ValueError):
            d.pop_front()

    def test_pop_back(self):
        d = Deque(['A', 'B', 'C'])
        assert d.pop_back() == 'C'
        assert d.length() == 2
        assert d.pop_back() == 'B'
        assert d.length() == 1
        assert d.pop_back() == 'A'
        assert d.length() == 0
        assert d.is_empty() is True
        with self.assertRaises(ValueError):
            d.pop_back()
