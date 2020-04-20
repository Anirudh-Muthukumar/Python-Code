class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None  


def bstFromPreorder(preOrder):
    stack = []
    A = preOrder[:]
    index = 0
    root = Node(A[index]) # create the root node
    index += 1
    stack.append(root)
    prev_val = root.val


    # construct left of most nodes
    while index<len(A) and A[index]<stack[-1].val:
        node = Node(A[index])   # create new node
        stack[-1].left = node   # make it left node of top of stack
        stack.append(node)      # add the node to stack
        index+=1    # move to next node
    
    # construct right subtrees of subtrees nodes in stack
    while A[index] < root.val and index<len(A):
        while A[index]<root.val and index<len(A) and A[index]>stack[-1].val:
            prev_node = stack.pop()
        prev_node.right = Node(A[index])
        index += 1
    



preOrder = [8, 5, 1, 7, 10, 12]
stack = []

if __name__ == '__main__':
    bstFromPreorder(preOrder)
    