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

    def remove_duplicates(self):
        data = []
        mover = self.head
        data.append(mover.data)
        while mover.next != None:
            if mover.next.data not in data:
                data.append(mover.next.data)
                mover = mover.next
            else:
                mover.next = mover.next.next

def append_node(l, node):
    pointer = l.head
    while pointer.next != None:
        pointer = pointer.next
    pointer.next = node

if __name__ == '__main__':
    data = random.sample(range(1, 1000), 30)
    data.extend(data)
    data.extend(data)
    print(data)
    nodes = []
    for d in data:
        nodes.append(Node(d))
    l = LinkedList()
    l.head = nodes[0]
    for node in nodes[1:]:
        append_node(l, node)
    print("List before removing duplicates")
    l.printlist()
    print("List after removing duplicates")
    l.remove_duplicates()
    l.printlist()
