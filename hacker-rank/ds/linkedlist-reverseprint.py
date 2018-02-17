"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""


def ReversePrint(head):
    if head is None:
        return head
    elems = []
    while head is not None:
        elems.append(head.data)
        head = head.next
    for elem in reversed(elems):
        print(elem)
