class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return
    # create a queue
    queue = []
    dis = []
    temp = [root.val]
    dis.append(temp)
    queue.append(root)

    while len(queue)>0:
        print(queue[0].val)
        temp = queue[0].val
        dis.append(temp)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        dis.append()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

bfs(root)