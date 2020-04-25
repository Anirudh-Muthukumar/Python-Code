'''
Time complexity : O(n)
Space complexity: O(h)  - height of tree
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None  

def Postorder(root):
    output = []
    stack = [root]
    while root or stack:
        if root:
            stack.append(root)
            root = root.left  
        else:
            temp = stack[-1].right 

            if not temp: # top of stack is a leaf node
                temp = stack.pop()
                output += [temp.val] # visit the node
                # check if visited node is the right child of top of stack
                while stack and stack[-1].right == temp:  
                    temp = stack.pop() # visited both left and right child, so visit the node
                    output += [temp.val]  

            else: # top of stack still has right child
                root = temp
             
            
    
    print("Postorder traversal = ", output)


if __name__ == '__main__':
    node8 = Node(8)
    node5 = Node(5)
    node1 = Node(1)
    node4 = Node(4)
    node6 = Node(6)
    node7 = Node(7)
    node10 = Node(10)
    node9 = Node(9)
    node12 = Node(12)


    root = node8
    node8.left = node5 ; node8.right = node10 
    node5.left = node1 ; node5.right = node7; 
    node10.left = node9 ; node10.right = node12
    node1.right = node4 
    node7.left = node6  

    Postorder(root)