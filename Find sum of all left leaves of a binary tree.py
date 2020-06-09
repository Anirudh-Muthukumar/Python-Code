class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None  


def sumLeftLeaf(root):
    if not root:
        return 0
    
    res = 0
    q = [(root, False)]

    while q:
        node, isLeftChild = q.pop(0)

        if not node.left and not node.right and isLeftChild:
            res += node.val 
            continue
        
        if node.left:
            q += (node.left, True),
        if node.right:
            q += (node.right, False),
    
    print("Sum = ", res)


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
    node2.left = node4; node2.right = node5;
    node3.left = node6; node3.right = node7;
    node4.right = node8; node8.left = node9;

    sumLeftLeaf(root)
    