from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.connected = {i:i+1 for i in range(n)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

n, q = map(int, input().split())
uf=UnionFind(n)

for _ in range(q):
    query=input().split()
    team1=int(query[1])-1
    team2=int(query[2])-1

    if query[0]=='1':
        uf.union(team1, team2)
    elif query[0]=='2':
        while team1 < team2:
            uf.union(team1, team2)
            nxt = uf.connected[team1]
            uf.connected[team1]=team2
            team1=nxt
    else:
        if uf.find(team1)==uf.find(team2):
            print("YES") 
        else:
            print("NO")
