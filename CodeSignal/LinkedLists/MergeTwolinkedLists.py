'''
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.
Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.
'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    curr1=l1
    curr2=l2
    # Edge Case - No values in list
    if l1==None:
        return l2
    if l2==None:
        return l1

    # Set first element
    if curr1.value<=curr2.value:
        new_list=curr1
        curr1=curr1.next
    else:
        new_list=curr2
        curr2=curr2.next

    # Loop until one list runs out
    curr_new=new_list
    while curr1!=None and curr2!=None:
        # Compare and add the lowest
        if curr1.value<=curr2.value:
            curr_new.next=curr1
            curr1=curr1.next
            curr_new=curr_new.next
        else:
            curr_new.next=curr2
            curr2=curr2.next
            curr_new=curr_new.next
    # Add the rest if not
    if curr1==None:
        curr_new.next=curr2
    elif curr2==None:
        curr_new.next=curr1

    #Return completed list
    return new_list