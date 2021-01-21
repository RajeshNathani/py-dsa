from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size_of(self):
        return len(self.container)


s = Stack()
s.push(5)
s.push(10)
s.push(15)
print(s)
print(s.size_of())
s.pop()
print(s.size_of())
print(s.is_empty())
