class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.size = [1] * n

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]

n = int(input())
distant_relatives = list(map(int, input().split()))

uf = UnionFind(n+1)

for i in range(n):
    uf.union(i+1, distant_relatives[i])

tree_cnt = 0
for i in range(1, n+1):
    if uf.find(i) == i:
        tree_cnt += 1

print(tree_cnt)