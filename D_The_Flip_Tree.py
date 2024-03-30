import sys, threading
from collections import defaultdict

ans = []

def main():
    num_nodes = int(input())
    graph = defaultdict(list)
    for _ in range(num_nodes - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    initial_values = list(map(int, input().split()))
    target_values = list(map(int, input().split()))
    
    def dfs(node, level, even_ops, odd_ops):
        visited_nodes[node] = True

        if level % 2 == 0:
            curr_value = (initial_values[node - 1] + even_ops) % 2
        else:
            curr_value = (initial_values[node - 1] + odd_ops) % 2

        if curr_value != target_values[node - 1]:
            ans.append(node)
            if level % 2 == 0:
                even_ops += 1
            else:
                odd_ops += 1

        for child in graph[node]:
            if not visited_nodes[child]:
                dfs(child, level + 1, even_ops, odd_ops)


    visited_nodes = [False] * (num_nodes + 1)
    dfs(1,0,0,0)

    print(len(ans))
    for node in ans:
        print(node)


if __name__ == "__main__":
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
