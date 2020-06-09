# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        
        res = []
        stack = []
        
        while stack or root:
            if root:
                stack += root,
                root = root.left
            else:
                temp = stack[-1].right
                
                if not temp: # top of stack is a leaf node
                    temp = stack.pop()
                    res += temp.val,
                    
                    while stack and stack[-1].right==temp: # check if visited node is right child of top of stack 
                        temp = stack.pop()
                        res += temp.val,     # visit the top of stack
                    
                else:  # explore the right child
                    root = temp
                        
        
        return res
                    