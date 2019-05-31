# list
class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fill_value=None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        for count in range(capacity):
            self._items.append(fill_value)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self._items[index]

    def __setitem__(self, index, new_item):
        """Subscript operator for replacement at index."""
        self._items[index] = new_item


class QueueList:
    def __init__(self):
        self._queue = list()

    def __len__(self):
        return len(self._queue)

    def is_empty(self):
        return len(self._queue) == 0

    def add(self, item):
        self._queue.append(item)

    def pop(self):
        assert not self.is_empty(), 'queue is empty'
        return self._queue.pop(0)


class Node:
    def __init__(self, data, next=None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next


# array
class QueueArray:
    def __init__(self, max_size):
        self._size = 0
        self._front = 0
        self._rear = -1
        self._queue = Array(max_size)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == len(self._queue)

    def pop(self):
        pass

    def add(self, item):
        assert not self.is_full(), 'queue is full'
        max_size = len(self._queue)
        self._rear = (self._rear + 1) % max_size
        self._queue[self._rear] = item
        self._size += 1

    def pop(self):
        assert not self.is_empty(), 'queue is empty'
        item = self._queue[self._front]
        max_size = len(self._queue)
        self._front = (self._front + 1) % max_size
        self._size -= 1
        return item


class LinkedQueue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._front = node
        else:
            self._rear.next = node
        self._rear = node
        self._size += 1

    def pop(self):
        assert not self.is_empty(), 'queue is empty'
        item = self._front.data
        if self._front == self._rear:
            self._rear = None
        else:
            self._front = self._front.next
        self._size -= 1
        return item

    def is_empty(self):
        return self._size == 0

