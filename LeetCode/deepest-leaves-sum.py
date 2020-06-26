'''Given a binary tree, return the sum of values of its deepest leaves.

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        sum=0
        sum_level=0     
        stack=[]
        if root==None:
            return 0
        stack.append((root,0))
        
        while len(stack)>0:
            curr=stack.pop()
            curr_node=curr[0]
            curr_level=curr[1]
            if curr_node.left or curr_node.right:      
                if curr_node.right:
                    stack.append((curr_node.right,curr_level+1))
                if curr_node.left:
                    stack.append((curr_node.left,curr_level+1))                
            else:
                if curr_level>sum_level:
                    sum_level=curr_level
                    sum=curr_node.val
                elif curr_level==sum_level:
                    sum+=curr_node.val
        return sum