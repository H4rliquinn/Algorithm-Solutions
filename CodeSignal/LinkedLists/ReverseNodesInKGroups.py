'''
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.
'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    curr_pos=l
    curr_group_start=l
    end_last=None

    # Loop through LL
    while curr_pos != None:
        # check if enough elements for group
        check_pos=curr_pos
        for i in range(k):
            if check_pos==None:
                break
            check_pos=check_pos.next
        if check_pos==None:
            break
        # Reverse Elements up to k
        group_start=curr_pos
        for i in range(k-1):
            temp=curr_pos
            curr_pos=group_start.next
            group_start.next=curr_pos.next
            curr_pos.next=temp
        for i in range(k):
            curr_pos=curr_pos.next
    # Return original l
    return l