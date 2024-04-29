import sys
import threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    tree = defaultdict(list) 
    p_input = list(map(int, input().split()))

    for i in range(2, n + 1):
        tree[p_input[i - 2]].append(i)

    cv = [0] + list(map(int, input().split()))
    steps = 0

    def dfs(v, target_color):
        nonlocal steps, cv, tree  
        
        if cv[v] != target_color:
            steps += 1
            target_color = cv[v]
            
        for u in tree[v]:
            dfs(u, target_color)

    dfs(1, cv[1])  

    print(steps + 1)
    
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
