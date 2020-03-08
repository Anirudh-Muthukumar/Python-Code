# Dijsktra's Algorithm for shortest path from a given source to all the vertices in a graph
# Time Complexity: O(v^2) for matrix and O(E log V) for adjacency List

def minDistanceNode(dist, sptSet):
    minDist = float('inf')
    minIndex = -1 

    for node in range(len(dist)):
        if dist[node] < minDist and sptSet[node]==False:
            minDist = dist[node]
            minIndex = node
    
    return minIndex

def dijkstra(graph, source):
    n = len(graph)

    # Distance array to keep track of distance of each vertex from the source
    dist = [float('inf')] * n  

    dist[source] = 0 

    # Shortest Path Tree set - a boolean array to keep track of nodes added to shortest path tree
    sptSet = [False] * n 

    # Iterate through all nodes 
    for _ in range(n):
        
        # find the node with least distance 
        node = minDistanceNode(dist, sptSet) 

        # Add it to the shortest path tree
        sptSet[node] = True 

        # Update the distance of the node's neighbors
        for neighbor in range(n):
            if graph[node][neighbor] > 0 and sptSet[neighbor] == False and dist[neighbor] > dist[node] + graph[node][neighbor]:
                dist[neighbor] = dist[node] + graph[node][neighbor]
        
    print("Vertex \tDistance from Source")
    for node in range(n):
        print("%d \t%d" %(node, dist[node]))



if __name__ == '__main__':

    v = 9 # number of vertices

    graph = [
                [0, 4, 0, 0, 0, 0, 0, 8, 0], 
                [4, 0, 8, 0, 0, 0, 0, 11, 0], 
                [0, 8, 0, 7, 0, 4, 0, 0, 2], 
                [0, 0, 7, 0, 9, 14, 0, 0, 0], 
                [0, 0, 0, 9, 0, 10, 0, 0, 0], 
                [0, 0, 4, 14, 10, 0, 2, 0, 0], 
                [0, 0, 0, 0, 0, 2, 0, 1, 6], 
                [8, 11, 0, 0, 0, 0, 1, 0, 7], 
                [0, 0, 2, 0, 0, 0, 6, 7, 0] 
            ]
    
    source = 0 # source vertex
    dijkstra(graph, source)