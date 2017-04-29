import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        mover = self.head
        while mover.next != None:
            print(mover.data)
            mover = mover.next
        print(mover.data)

    def nth_last(self, n):
        mover = self.head
        i = 0
        while mover.next != None:
            mover = mover.next
            i += 1
        r = i - n
        if r < 0:
            print("Does not exist, n is greater than list size")
            return
        mover = self.head
        j = 0
        while j != r:
            mover = mover.next
            j += 1
        print(mover.data)


def append_node(l, node):
    pointer = l.head
    while pointer.next != None:
        pointer = pointer.next
    pointer.next = node

if __name__ == '__main__':
    data = random.sample(range(1, 1000), 6)
    print(data)
    nodes = []
    for d in data:
        nodes.append(Node(d))
    l = LinkedList()
    l.head = nodes[0]
    for node in nodes[1:]:
        append_node(l, node)
    n = random.choice(range(0, len(nodes) - 1))
    print("Finding nth(%s) to the last element" % n)
    l.nth_last(n)
