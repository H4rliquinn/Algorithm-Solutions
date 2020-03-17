"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head:
        curr=head
    else:
        return False
    while curr.next:
        if getattr(curr,'visited',False):
            return True
        curr.visited=True
        curr=curr.next
    return False