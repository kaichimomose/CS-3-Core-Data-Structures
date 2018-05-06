from doublylinkedlist import DoublyLinkedList

class LinkedDeque(object):

    def __init__(self, iterable=None):
        self.list = DoublyLinkedList()
        if iterable is not None:
            for item in iterable:
                self.push_back(item)

    def __repr__(self):
        """Return a string representation of this deque."""
        return 'Deque({} items, front={}, back={})'.format(self.length(), self.front(), self.back())

    def is_empty(self):
        """Return True if this deque is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this deque."""
        return self.list.size

    def push_front(self, item):
        """Insert the given item at the front of this deque.
        Running time: O(1) - add item front of the DoublyLinkedList"""
        self.list.prepend(item)

    def push_back(self, item):
        """Insert the given item at the back of this deque.
        Running time: O(1) - add item back of the DoublyLinkedList"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this deque without removing it,
        or None if this deque is empty."""
        if self.is_empty():
            return None
        else:
            return self.list.head.data

    def back(self):
        """Return the item at the back of this deque without removing it,
        or None if this deque is empty."""
        if self.is_empty():
            return None
        else:
            return self.list.tail.data

    def pop_front(self):
        """remove and return the item at the front of the deque.
        Running time: O(1) - delete item front of the DoublyLinkedList"""
        if self.is_empty():
            raise ValueError('This deque is empty.')
        else:
            data = self.front()
            self.list.head = self.list.head.next
            if self.list.head is None:
                self.list.tail = None
            else:
                self.list.head.previous = None
            self.list.size -= 1
            return data

    def pop_back(self):
        """remove and return the item at the back of the deque.
        Running time: O(1) - delete item back of the DoublyLinkedList"""
        if self.is_empty():
            raise ValueError('This deque is empty.')
        else:
            data = self.back()
            self.list.tail = self.list.tail.previous
            if self.list.tail is None:
                self.list.head = None
            else:
                self.list.tail.next = None
            self.list.size -= 1
            return data


Deque = LinkedDeque
