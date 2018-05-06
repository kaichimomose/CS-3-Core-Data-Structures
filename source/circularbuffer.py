class CircularBuffer(object):

    def __init__(self, max_size):
        self.list = [None] * max_size
        self.max_size = max_size
        self.size = 0
        self.start = 0
        self.end = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.size == self.max_size:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.is_full():
            raise ValueError('This circular buffer is full.')
        else:
            self.size += 1
            self.list[self.end] = item
            self.end += 1
            if self.end == self.max_size:
                self.end = 0

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.list[self.start]

    def dequeue(self):
        if self.is_empty():
            raise ValueError('This circular buffer is empty.')
        else:
            data = self.front()
            self.size -= 1
            # updates buffer start
            if self.start == (self.max_size - 1):
                self.start = 0
            else:
                self.start += 1
            return data
