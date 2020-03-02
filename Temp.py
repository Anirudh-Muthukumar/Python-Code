# Topsort
import collections

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = collections.defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def util(self, i, visited, stack):
        visited[i] = True

        for j in self.graph[i]:
            if not visited[j]:
                self.util(j, visited, stack)
        
        stack.insert(0, i)
    
    def topologicalSort(self):
        visited = [False for _ in range(self.V)]
        stack = list()
        for i in range(self.V):
            if not visited[i]:
                self.util(i, visited, stack)

        print("Topsort ordering: ", stack)

if __name__ == '__main__':

    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0) 
    g.addEdge(4, 1) 
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    # print(g.graph)
    g.topologicalSort()