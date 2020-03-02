def dfs(i, visited, stack):

    visited[i] = True
    
    if i+1<5 and not visited[i+1]:
        dfs(i+1, visited, stack)

    stack.append(i)

visited = [False for _ in range(5)]
stack = []
for i in range(5):
    if not visited[i]:
        dfs(0, visited, stack)

print(stack)