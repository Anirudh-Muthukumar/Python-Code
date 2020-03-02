# number of strokes required to paint given canvas
def isSafe(x, y, grid):
    return 0<=x<len(grid) and 0<=y<len(grid[0])

def dfs(x, y, grid, color):
    grid[x][y] = -1

    moveX = [0, 0, 1, -1]
    moveY = [1, -1, 0, 0]

    for i in range(4):
        if isSafe(x+moveX[i], y+moveY[i], grid) and grid[x+moveX[i]][y+moveY[i]]==color:
            dfs(x+moveX[i], y+moveY[i], grid, color)


def countStrokes(grid):
    n, m = len(grid), len(grid[0])
    ct = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]!=-1:
                dfs(i, j, grid, grid[i][j])
                ct+=1
    
    print("No. of strokes = ", ct)
    

grid = [[1,1,1,3,3],
        [1,5,1,3,3],
        [1,2,1,3,3]
    ]

countStrokes(grid)
