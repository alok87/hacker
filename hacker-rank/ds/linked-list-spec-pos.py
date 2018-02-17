#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""


def GetNode(head, position):
    if head is None:
        return None
    n = 0
    top_head = head
    while head:
        n += 1
        head = head.next
    pos = n - position

    i = 0
    while top_head:
        if i == pos - 1:
            return top_head.data
        i += 1
        top_head = top_head.next
    return None
