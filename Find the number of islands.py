class Graph:

    def __init__(self, row, col, graph):
        self.graph = graph
        self.row = row
        self.col = col
    

    def isSafe(self, x, y):
        return x>=0 and x<self.row and y>=0 and y<self.col


    def DFSUtil(self, row, col, visited):
        
        visited[row][col] = True

        # check neighbors in 8 directions
        x_dir = [-1, -1, -1, 0, 0, 1, 1, 1]
        y_dir = [-1, 0, 1, -1, 1, -1, 0, 1]

        # counting adjacent 1s and marking them visited
        for i in range(8):
            if self.isSafe(row + x_dir[i], col + y_dir[i]) and not visited[row + x_dir[i]][col + y_dir[i]] and self.graph[row][col]==1:
                self.DFSUtil(row + x_dir[i], col + y_dir[i], visited)

    def countIslands(self,):

        # visited list to check island is already visited
        visited = [ [False for _ in range(self.col)] for _ in range(self.row) ]
        ct = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.graph[i][j]==1 and visited[i][j]==False:
                    # print("here")
                    self.DFSUtil(i, j, visited)
                    ct += 1
        return ct

if __name__ == '__main__':
    graph = [[1, 1, 0, 0, 0], 
            [0, 1, 0, 0, 1], 
            [1, 0, 0, 1, 1], 
            [0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 1]] 


    row = len(graph) 
    col = len(graph[0]) 

    g = Graph(row, col, graph) 

    print("Number of islands is:", g.countIslands())