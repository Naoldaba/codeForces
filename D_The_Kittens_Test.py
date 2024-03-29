# class UnionFind:
#     def __init__(self, n):
#         self.parent = [-1] * n
#         self.last_ind = list(range(n))
#         self.nxt_ind = [-1] * n

#     def find(self, root_x):
#         if self.parent[root_x] < 0:
#             return root_x
#         self.parent[root_x] = self.find(self.parent[root_x])
#         return self.parent[root_x]

#     def union(self, x, y):
#         root_x = self.find(x)
#         root_y = self.find(y)
#         if root_x != root_y:
#             if self.parent[root_y] < self.parent[root_x]:
#                 root_x, root_y = root_y, root_x
#             self.parent[root_x] += self.parent[root_y]
#             self.parent[root_y] = root_x
#             self.nxt_ind[self.last_ind[root_x]] = root_y
#             self.last_ind[root_x] = self.last_ind[root_y]

# n = int(input())
# uf = UnionFind(n + 1)
# for _ in range(n - 1):
#     u, v= map(int,input().split())
#     uf.union(u, v)

# i = uf.find(2)
# ans=[]
# while i != -1:
#     ans.append(i)
#     i = uf.nxt_ind[i]
    
# print(*ans)

import sys
input = sys.stdin.readline

def find(x):
    curr = x
    while curr != parent[curr]:
        curr = parent[curr]
    
    while x != parent[x]:
        nxt = parent[x]
        parent[x] = curr
        x = nxt
    
    return x

def union(x, y):
    X, Y = find(x), find(y)
    if Y < X:
        X, Y = Y, X

    parent[Y] = X
    arr[X] += arr[Y]
    arr[Y] = []

N = int(input())
parent = [i for i in range(N)]
arr = [[i + 1] for i in range(N)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    union(x - 1, y - 1)

print(*arr[0])
