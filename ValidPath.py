grid = [ 
            ['W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W'],
]

def validPath(grid, w, l, wee, lee):
    q = [(w, l)]
    visited = set()
    visited.add((w, l)) 

    while q:
        x, y = q.pop(0)
        
        for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if i==wee and j==lee:
                return True

            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]!='W' and (i, j) not in visited:
                q.append((i, j))
                visited.add((i, j))
    
    return False

def getHash(grid):
    val = ""  
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val += grid[i][j] + ','
    return val   

def removeWalls(grid, w, l, wee, lee):
    # for BFS
    q = [grid]

    # to keep track of visited states
    visited = set()
    visited.add(getHash(grid))

    while q:
        state = q.pop(0)  
        print("Parent : ")  
        for i in range(len(grid)):
            print(state[i])

        if validPath(state, w, l, wee, lee):
            print("Found solution : ")
            for i in range(len(grid)):
                print(state[i])
            return   
        
        new_state = [x[:] for x in state[:]]

        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if new_state[i][j]=='W':
                    temp_state = [x[:] for x in new_state]
                    temp_state[i][j]='F'
                    # print()
                    # for i in range(len(grid)):
                    #     print(temp_state[i])
                    # print()
                    if getHash(temp_state) not in visited:
                        visited.add(getHash(temp_state))
                        q.append(temp_state)
                    # new_state[i][j] = 'W'
            
        
    print("No solution found !!!")

lookup = [[0 for _ in range(100)] for _ in range(100)]
w, l = 1, 0
wee, lee = 0, 2
if not validPath(grid, w, l, wee, lee):
    print("No valid path!!")
    removeWalls(grid, w, l, wee, lee)
