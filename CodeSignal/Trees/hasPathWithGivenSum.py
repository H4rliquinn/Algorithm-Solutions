"""
Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    # Return if Empty edge case
    if t==None:
        return s==0
    ret_val=False
    # Calculate current value remaining
    new_sum=s-t.value

    # If sum is correct at leaf return True
    if t.left==None and t.right==None:
        if new_sum==0:
            return True
    # Move down if possible
    if t.left!=None:
        new_val=hasPathWithGivenSum(t.left,new_sum)
        if new_val or ret_val:
            ret_val=True
    if t.right!=None:
        new_val=hasPathWithGivenSum(t.right,new_sum)
        if new_val or ret_val:
            ret_val=True

    return ret_val
