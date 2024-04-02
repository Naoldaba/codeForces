from collections import defaultdict, deque
import heapq

n, m = map(int, input().split())
graph = defaultdict(list)
indegree = defaultdict(int)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

queue = []
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    cur = heapq.heappop(queue)
    result.append(cur)
    for child in graph[cur]:
        indegree[child] -= 1
        if indegree[child] == 0:
            heapq.heappush(queue, child)

if len(result) != n:
    print(-1)
else:
    print(*result)