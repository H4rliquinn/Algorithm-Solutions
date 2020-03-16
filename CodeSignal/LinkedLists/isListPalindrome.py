# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def find_linked_list_length(l):
    current = l
    length = 0
    while current:
        length += 1
        current = current.next
    return length

# input is a linked list
# output is a boolean 
def isListPalindrome(l):
    length = find_linked_list_length(l)
    if length==0:
        return True
    a = l
    a.prev = None

    # advance a to the midpoint of the list
    for _ in range(length // 2):
        # set up previous pointers
        prev = a
        a = a.next
        a.prev = prev

    # init b to the same node as a
    if length%2==0:
        b = a.prev
    else:
        b=a.prev
        a=a.next

    # traverse both a and b until a reaches the end of the list
    while a:
        # print(a.value,b.value)
        if a.value != b.value:
            return False
        a = a.next
        b = b.prev

    return True
