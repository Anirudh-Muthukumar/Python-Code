class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None  

def countNodes(root):
    if not root:
        return 0
    return (1 + countNodes(root.left) + countNodes(root.right))

def isCompleteUtil(root, index, total):
    if not root:
        return True

    if index>=total:
        return False
    
    return isCompleteUtil(root.left, 2*index+1, total) and isCompleteUtil(root.right, 2*index+2, total)

def isCompleteBT(root): 
    # All the levels are coompletely filled except the last level
    # The last level should be filled from left to right
    total = countNodes(root)
    return isCompleteUtil(root, 0, total)
        


if __name__ == '__main__':
    node8 = Node(8)
    node5 = Node(5)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node6 = Node(6)
    node7 = Node(7)
    node10 = Node(10)
    node9 = Node(9)
    node12 = Node(12)
    node0 = Node(0)


    root = node1 
    root.left = node2; root.right = node3;
    # node1.left = node3; node1.right = node4;
    node2.left = node4; node2.right = node5;
    node3.left = node6; node3.right = node7;


    print("Complete binary tree = ", isCompleteBT(root))