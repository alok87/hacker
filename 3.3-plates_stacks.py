import random


class Set_of_stacks:
    def __init__(self):
        self.index = 0
        self.stack_num = 0
        self.max_index = 9
        self.stacks = {}

    def push(self, data):
        if self.index == self.max_index:
            self.stack_num += 1
        if self.stack_num not in self.stacks:
            self.stacks[self.stack_num] = []
        self.stacks[self.stack_num].append(data)
        self.index = len(self.stacks[self.stack_num]) - 1
        print("Pushed: %d\tPlatesSet-%d: %s\n" % (data, self.stack_num+1, self.stacks[self.stack_num]))
        return data

    def pop(self):
        if self.index < 0:
            self.stacks[self.stack_num] = None
            self.stack_num -= 1
        if self.stack_num < 0:
            return None
        popped = self.stacks[self.stack_num].pop()
        self.index = len(self.stacks[self.stack_num]) - 1
        print("Popped: %d\tPlatesSet-%d: %s\n" % (popped, self.stack_num+1, self.stacks[self.stack_num]))
        return popped


if __name__ == '__main__':
    s = Set_of_stacks()

    for data in random.sample(range(0, 100), 40):
        s.push(data)

    while s.pop():
        pass
