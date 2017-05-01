import random


class Stack:
    def __init__(self):
        self.top = 0
        self.min = None
        self.min_stack = []
        self.stack = []

    def push(self, data):
        if len(self.stack) == 0:
            self.min = data
            self.min_stack.append(self.min)
        if data < self.min:
            self.min = data
            self.min_stack.append(self.min)
        self.stack.append(data)
        self.top = len(self.stack) - 1
        print("Pushed: %d\nStack: %s\nMin: %d\n\n" % (data,
                                                      self.stack,
                                                      self.min))
        return data

    def pop(self):
        popped = self.stack.pop()
        if popped == self.min:
            self.min_stack.pop()
            self.min = self.min_stack[len(self.min_stack)-1]
        print("Popped %d,\nStack: %s,\nMin: %d\n\n" % (popped,
                                                       self.stack,
                                                       self.min))
        return popped


s = Stack()
for data in random.sample(range(0, 100), 10):
    s.push(data)
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
