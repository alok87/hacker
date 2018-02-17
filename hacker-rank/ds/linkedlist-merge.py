"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def MergeLists(headA, headB):
    e = []
    while headA:
        e.append(headA.data)
        headA = headA.next
    while headB:
        e.append(headB.data)
        headB = headB.next
    elems = sorted(e)
    head = None
    top_head = None
    for elem in elems:
        if head is None:
            head = Node(data=elem)
            top_head = head
            continue
        head.next = Node(data=elem)
        head = head.next
    return top_head
