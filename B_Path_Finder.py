from collections import defaultdict

test = int(input())
graph = defaultdict(set)
dist_arr = [0] * test

for _ in range(test-1):
    u, v, c = map(int, input().split())
    graph[u].add((v, c))
    graph[v].add((u, c))


def dfs(node, parent):
    for child, cost in graph[node]:
        if child != parent:
            dist_arr[child] = dist_arr[node] + cost
            dfs(child, node)

dfs(0, -1)
Max_di = max(dist_arr)
print(Max_di)