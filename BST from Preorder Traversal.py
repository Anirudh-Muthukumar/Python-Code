'''
# 1. Create empty stack and push root
# 2. Keep popping stack until stack is not empty and preorder[i] > stack.top()
# 3. Make it left/right child and push it into stack
# 4. Repeat 2, 3 until stack is empty

Time complexity : O(n)
Space complexity: O(h)
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None  



def bstFromPreorder(preorder):
    stack = []
    root = Node(preorder[0])
    stack.append(root)

    for i in range(1, len(preorder)):
        temp = None 

        while stack and preorder[i] > stack[-1].val:
            temp = stack.pop()  
        
        # If some element was popped from stack it is right child
        if temp:
            temp.right = Node(preorder[i])
            stack.append(temp.right)
        
        else:  # it is a left child
            stack[-1].left = Node(preorder[i])
            stack.append(stack[-1].left)

    print(root.val)



preOrder = [8, 5, 1, 7, 10, 12]
stack = []

if __name__ == '__main__':
    bstFromPreorder(preOrder)
    