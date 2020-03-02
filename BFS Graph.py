graph = {}

def addEdge(u, v):
    if u not in graph:
        graph[u] = []
    graph[u].append(v)


def BFS(start):
    visited = [False] * N

    queue = [start]
    visited[start] = True
    output = []

    while queue:
        node = queue.pop(0)
        output.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue += [neighbor]
                visited[neighbor] = True
    
    return output
                

if __name__ == '__main__':

    N = 4
    addEdge(0, 1) 
    addEdge(0, 2) 
    addEdge(1, 2) 
    addEdge(2, 0) 
    addEdge(2, 3) 
    addEdge(3, 3)

    nodes = BFS(2)
    print("BFS Traversal of graph : ", nodes)