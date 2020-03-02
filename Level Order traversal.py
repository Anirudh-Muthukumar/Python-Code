class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return
    queue = [root]
    res, temp = [], []
    while queue:
        for i in range(len(queue)):
            node = queue.pop(0)
            temp += [node.val]
            if node.left:
                queue += [node.left]
            if node.right:
                queue += [node.right]
        res.append(temp)
        temp = []
    
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Level order traversal : ")
for temp in bfs(root):
    print(temp)