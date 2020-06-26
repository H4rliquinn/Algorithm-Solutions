'''Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
If there are no nodes with an even-valued grandparent, return 0.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class Solution:

    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = queue.Queue(maxsize=0)
        kids=queue.Queue(maxsize=0)
        # q.put()
        # q.get()
        sum=0
        if root==None:
            return 0
        q.put(root)
        while q.empty()==False:
            grandpa=q.get()
            if grandpa.val%2==0:
                if grandpa.left!=None:
                    kids.put(grandpa.left)
                if grandpa.right!=None:
                    kids.put(grandpa.right)
                while kids.empty()==False:
                    kid=kids.get()
                    if kid.left!=None:
                        sum+=kid.left.val
                    if kid.right!=None:
                        sum+=kid.right.val
            if grandpa.left:
                q.put(grandpa.left)
            if grandpa.right:
                q.put(grandpa.right)
        return sum