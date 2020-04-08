# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    curr_a=a
    curr_b=b
    str_a=''
    str_b=''
    

    while curr_a is not None:
        val=str(curr_a.value)
        str_a+=f'{"0"*(4-len(val))}{val}'
        curr_a=curr_a.next

    while curr_b is not None:
        val=str(curr_b.value)
        str_b+=f'{"0"*(4-len(val))}{val}'
        curr_b=curr_b.next

    print(int(str_a),int(str_b))