class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None  


def noSibling(root):
    res = []
    q = [root]

    while q:
        node = q.pop(0)

        if node.left and node.right: # node has two children
            q.append(node.left)
            q.append(node.right)
            continue

        if node.left:  # node has one child
            q.append(node.left)
            res.append(node.left.val)
        if node.right:  # node has one child
            q.append(node.right)
            res.append(node.right.val)
    
    print("Single child nodes: ", res)



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


    root = node0 
    root.left = node1; root.right = node2;
    node1.left = node3; node1.right = node4;
    node2.left = node5; node5.right = node7;
    node3.right = node6; node6.right = node8;


    noSibling(root)