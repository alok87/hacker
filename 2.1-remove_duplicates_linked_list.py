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

def append_node(l, node):
    pointer = l.head
    while pointer.next != None:
        pointer = pointer.next
    pointer.next = node

if __name__ == '__main__':
    data = random.sample(range(1, 100), 10)
    print(data)
    nodes = []
    for d in data:
        nodes.append(Node(d))
    l = LinkedList()
    l.head = nodes[0]
    for node in nodes[1:]:
        append_node(l, node)
    l.printlist()
