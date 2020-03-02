graph = {}
queue = []
visited = []
m, n = None, None

def toStr(node):
    string = ""
    for i in range(len(node)):
        for j in range(len(node[0])):
            string += str(node[i][j])
    return string

def toMatrix(string):
    matrix = [ [0 for _ in range(n)] for _ in range(m)]
    for ind, ch in enumerate(string):
        matrix[ind//n][ind%n] = int(ch)
    return matrix

def addEdge(node_str):
    node = toMatrix(node_str)
    neighbors = []

    # if node_str == reqd_str:
    #     return 1

    # if node_str not in graph:
    #     graph[node_str] = []
    
    # if node_str in visited:
    #     return None

    for i in range(m):
        for j in range(n):
            x, y = i, j
            new_node = node
            if 0<=x<m and 0<=y<n: # (x,y)
                new_node[x][y] = (node[x][y]+1)%2
            if 0<=x-1<m and 0<=y<n: # (x-1,y)
                new_node[x-1][y] = (node[x-1][y]+1)%2
            if 0<=x+1<m and 0<=y<n: # (x+1, y)
                new_node[x+1][y] = (node[x+1][y]+1)%2
            if 0<=x<m and 0<=y-1<n: # (x, y-1)
                new_node[x][y-1] = (node[x][y-1]+1)%2
            if 0<=x<m and 0<=y+1<n: # (x, y+1)
                new_node[x][y+1] = (node[x][y+1]+1)%2

            new_node_str = toStr(new_node)
            if new_node_str not in visited:
                neighbors += [new_node_str]

    return neighbors


    #         if new_node_str not in visited:
    #             graph[node_str].append(new_node_str)
    #             queue.add
    #             visited += [new_node] 

    # return None
new_visited = []

def dfs(source, ct):
    
    if source==reqd_str:
        print("Found again")
        return ct

    for nei in graph[source]:
        # print(nei)
        if nei not in new_visited:
            new_visited.append(nei)
            return dfs(nei, ct+1)

    return -1

if __name__ == '__main__':
    # m, n = 3, 3
    # string = "111101000"
    # reqd_str = "000000000"

    m, n = 2, 2
    string = "0001"
    reqd_str = "0000"


    queue.append(string)
    visited += [string]
    flag = False
    size_graph = 1
    level = {}
    level[string] = 0
    new_visited += [[string]]
    while queue :
        source = queue.pop(0)
        neighbors = addEdge(source)
        size_graph += len(neighbors)
        if source not in graph:
            graph[source] = []

        new_visited += [neighbors]

        for neighbor in neighbors:
            level[neighbor] = level[source] + 1

            if neighbor==reqd_str:
                graph[source].append(neighbor)
                print("Steps = ", level[source]+1)
                print("Found")
                flag = True
                break

            if neighbor not in visited:
                graph[source].append(neighbor)
                queue.append(neighbor)
                visited.append(neighbor)
            
    print(new_visited)
    # print("Size of graph = ", size_graph)

    # new_visited.append("111101000")
    # ans = dfs("111101000", 0)
            
    # print("Levels : ", levels)
    # print(graph)
   
    # print("Steps = ", level[reqd_str])
        


            

    