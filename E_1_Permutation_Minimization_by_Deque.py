from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())

    ret = deque()
    mn = float('inf')
    pi = list(map(int, input().split()))
    for i in range(n):
        
        mn = min(mn, pi[i])

        if mn == pi[i]:
            ret.appendleft(pi[i])
        else:
            ret.append(pi[i])

    print(' '.join(map(str, ret)))