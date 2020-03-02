# Program to find the path to reach bottom-right from top-left such that
# sum of all elements in its path is minimum 

grid = [[1,3,1],[1,5,1],[4,2,1]]

row, col = len(grid), len(grid[0])

for j in range(1, col):
    grid[0][j] += grid[0][j-1]
for i in range(1, row):
    grid[i][0] += grid[i-1][0]
for i in range(1, row):
    for j in range(1, col):
        grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
print("Minimum path sum = {}".format(grid[row-1][col-1]))