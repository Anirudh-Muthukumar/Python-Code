g1 = {}

def addEdge(u, v):
    if u not in g1:
        g1[u] = []
    g1[u].append(v)

def dfs(node, visited):
    visited[node] = True

    if node not in g1:
        return

    for nei in g1[node]:
        if not visited[nei]:
            dfs(nei, visited)

def isConnected():
    visited = [ False for _ in range(5)]

    dfs(1, visited) # if graph is connected, this will end up reaching all other nodes
    
    for i in range(1, len(visited)):
        if not visited[i]:          # even if one node is unreachable from someother node in graph, it is not connected
            return False

    return True

addEdge(1, 2)
addEdge(1, 3)
addEdge(2, 3)
addEdge(4, 4)



if isConnected():
    print("Yes")
else :
    print("No")