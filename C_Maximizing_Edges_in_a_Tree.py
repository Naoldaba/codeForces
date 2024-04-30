from collections import defaultdict
import sys, threading

graph = defaultdict(list)
visited = []
side = [0, 0]

def main():
    global graph, visited, side
    side = [0, 0]
    n = int(input())
    visited = [1] * (n + 1)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append((v, 0))
        graph[v].append((u, 0))

    dfs(1, 0)
    print(side[0] * side[1] - (n - 1))


def dfs(node, side_idx):

    global side
    side[side_idx] += 1
    visited[node] = 0
    for neighbor, _ in graph[node]:
        if visited[neighbor]:
            dfs(neighbor, 1 - side_idx)


if __name__ == "__main__":
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
