# Two nodes are cousins if they have same depth but different parents

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def cousins(x, y, root):
    if root is None:
        return 
    queue, res, temp = [root], [], []
    parent = {root.val:None}
    while queue:
        for i in range(len(queue)):
            node = queue.pop(0)
            temp += [node.val]
            if node.left:
                queue += [node.left]
                parent[node.left.val] = node
            if node.right:
                queue += [node.right]
                parent[node.right.val] = node
        res += [temp]
        temp = []


    for temp in res:
        if x in temp and y in temp and parent[x]!=parent[y]:
            return True

    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Nodes 2 and 4 are cousins :", cousins(2, 4, root))
print("Nodes 5 and 7 are cousins :", cousins(5, 7, root))
print("Nodes 2 and 3 are cousins :", cousins(2, 3, root))