class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialise(root):
    arr = []

    def encode(node):
        if node:
            arr.append(str(node.val))
            encode(node.left)
            encode(node.right)
        else:   # to indicate Null values
            arr.append('#')
    
    encode(root)
    return arr 

def deserialise(data):

    def decode(vals):
        val = next(vals)

        if val=='#':
            return None 

        node = Node(int(val))
        node.left = decode(vals)
        node.right = decode(vals)

        return node 
    
    vals = iter(data.split()) # to traverse the container exactly once 
    return decode(vals)

if __name__ == '__main__':
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    root = node1
    root.left = node2
    root.right = node3

    node2.left = node4 
    node2.right = node5 

    node4.left = node6 

    arr = serialise(root)
    data = ' '.join(arr)
    print("Serialised BT: ", data)

    
    vals = iter(data.split())

    node = deserialise(data)
    
    print(node.val)
    print(node.left.val)
    print(node.right.val)