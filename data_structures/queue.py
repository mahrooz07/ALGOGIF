class Node:
    """A node in the queue."""
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """Queue data structure using linked nodes."""
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, value):
        """Add an element to the rear of the queue."""
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = self.rear
        self._size += 1

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if not self.front:
            return None  # Queue is empty
        dequeued_value = self.front.data
        self.front = self.front.next
        if not self.front:  # Queue becomes empty
            self.rear = None
        self._size -= 1
        return dequeued_value

    def peek(self):
        """Return the front element without removing it."""
        return self.front.data if self.front else None

    def size(self):
        """Return the number of elements in the queue."""
        return self._size

    def display(self):
        """Return a list of all elements in the queue."""
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return elements
