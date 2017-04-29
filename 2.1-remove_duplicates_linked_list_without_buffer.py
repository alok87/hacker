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
        previous = self.head
        current = self.head.next
        while current != None:
            mover = self.head
            while mover != current:
                if mover.data == current.data:
                    current = current.next
                    previous.next = current
                    break
                mover = mover.next
            if mover == current:
                previous = current
                current = current.next


def append_node(l, node):
    pointer = l.head
    while pointer.next != None:
        pointer = pointer.next
    pointer.next = node

if __name__ == '__main__':
    data = random.sample(range(1, 1000), 3)
    data.extend(data)
    #data.extend(data)
    print(data)
    data = [68, 737, 278, 68, 68, 278]
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
