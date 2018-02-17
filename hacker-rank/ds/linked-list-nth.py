"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
# This is a "method-only" submission.
# You only need to complete this method.


def InsertNth(head, data, position):
    if head is None:
        return Node(data)
    pos = 0
    front = head
    prev = None
    while pos != position:
        prev = head
        head = head.next
        pos += 1
    if prev is None:
        prev = Node(data, front)
        return prev
    prev.next = Node(data, head)
    return front
