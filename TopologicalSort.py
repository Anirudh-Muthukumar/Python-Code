# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of its vertices such
# that for every directed edge uv, vertex u comes before vertex v in the ordering. 
# Used to visual dependencies 

# Function to check graph contains cycle or not

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, i, visited, stack):
        visited[i] = True

        for nei in self.graph[i]:
            if not visited[nei]:
                self.topologicalSortUtil(nei, visited, stack)
        
        stack.insert(0, i)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = list()

        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        
        print("Topological sort : ", stack)
    
    def isCyclicUtil(self, i, visited, recStack):
        visited[i] = True
        recStack[i] = True

        for j in self.graph[i]:
            if not visited[j]:
                if self.isCyclicUtil(j, visited, recStack):
                    return True
            elif recStack[j]:
                return True 

        # backtrack
        recStack[i] = False
        return False
    
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                if self.isCyclicUtil(i, visited, recStack):
                    return True
        
        return False

if __name__ == "__main__":

    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0) 
    g.addEdge(4, 1) 
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    # print(g.graph)
    g.topologicalSort()

    g = Graph(2)
    g.addEdge(0, 1)
    # g.addEdge(1, 0)
    print("Does graph contain cycle ? - ", g.isCyclic())