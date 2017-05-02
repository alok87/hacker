import random
import time


def move(t1, t2, t3):
    total_disks = t1.disks()
    while t2.disks() != total_disks or t3.disks != total_disks:
        print("Run: %s, %s, %s" % (t1.stack, t2.stack, t3.stack))
        elem = t1.top()
        if not t2.top:
            t2.push(t1.pop())
            continue
        if not t3.top:
            t3.push(t1.pop())
            continue
        while t2.stack
        time.sleep(10)


class Tower:
    def __init__(self):
        self.top = None
        self.stack = []

    def disks(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)
        self.top = data
        #print("Pushed: %d\nStack: %s\n\n" % (data, self.stack))
        return data

    def pop(self):
        popped = None
        try:
            popped = self.stack.pop()
            self.top = self.stack[-1]
        except:
            pass
        if not popped:
            self.top = None
        return popped


if __name__ == '__main__':
    t1 = Tower()
    for data in range(3, 0, -1):
        t1.push(data)
    t2 = Tower()
    t3 = Tower()
    print("-----Tower of hanoi-----\n")
    print("Tower1: %s" % t1.stack)
    print("Tower2: %s" % t2.stack)
    print("Tower3: %s\n" % t3.stack)
    move(t1, t2, t3)
    print("Tower1: %s" % t1.stack)
    print("Tower2: %s" % t2.stack)
    print("Tower3: %s" % t3.stack)
