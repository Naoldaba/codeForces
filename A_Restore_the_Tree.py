from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(list)
indegre = defaultdict(int)

for _ in range(n+m-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegre[v]+=1

queue=deque()
for i in range(1, n+1):
    if indegre[i]==0:
        queue.append(i)
        
ans=[0]*(n+1)

while queue:
    curr=queue.popleft()
    for child in graph[curr]:
        indegre[child]-=1
        if indegre[child]==0:
            ans[child]=curr
            queue.append(child)
for i in range(1, n+1):
    print(ans[i])
