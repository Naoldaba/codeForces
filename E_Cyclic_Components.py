from collections import defaultdict

n, m =map(int, input().split())
graph=defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited=set()

def dfs(node):
    Stack=[node]
    visited.add(node)

    result = True

    while Stack:
        curr=Stack.pop()
        if len(graph[curr])!=2:
            result = False
        
        for neigbour in graph[curr]:
            if neigbour not in visited:
                visited.add(neigbour)
                Stack.append(neigbour)

    return result

count=0
for i in range(1, n+1):
    if i not in visited:
        if dfs(i):
            count+=1

print(count)