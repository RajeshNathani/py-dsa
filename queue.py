from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


q = Queue()
q.enqueue('5')
q.enqueue('10')
print(q.size())
q.dequeue()
print(q.size())
print(q.is_empty())
