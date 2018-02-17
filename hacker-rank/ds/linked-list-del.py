"""
 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Delete(head, position):
    if head is None:
        return head
    pos = 0
    front = head
    prev = None
    while pos != position:
        prev = head
        head = head.next
        pos += 1
    if prev is None:
        return head.next
    if head is None:
        prev.next = None
        return front
    prev.next = head.next
    return front
