
class UnionFind:
    def __init__(self, n):
        self.parent={i:i for i in range(n)}
        self.size=[1]*n
        self.Min=[i for i in range(n)]
        self.Max=[i for i in range(n)]

    def find(self, x):
        if x==self.parent[x]:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x=self.find(x)
        root_y=self.find(y)

        if root_x!=root_y:
            if self.size[root_x]<self.size[root_y]:
                self.parent[root_x]=root_y
                self.Min[root_y]=min(self.Min[root_x], self.Min[root_y])
                self.Max[root_y]=max(self.Max[root_x], self.Max[root_y])
                self.size[root_y]+=self.size[root_x]
            else:
                self.parent[root_y]=root_x
                self.Min[root_x]=min(self.Min[root_x], self.Min[root_y])
                self.Max[root_x]=max(self.Max[root_x], self.Max[root_y])
                self.size[root_x]+=self.size[root_y]


n, queries = map(int, input().split())

uf=UnionFind(n)
for _ in range(queries):
    query=list(input().split())
    # print(query)
    command=query[0]
    if command=="union":
        u, v = int(query[1])-1, int(query[2])-1
        if uf.find(u)!=uf.find(v):
            uf.union(u,v)
    else:
        v=int(query[1])-1
        parent=uf.find(v)
        print(uf.Min[parent]+1, uf.Max[parent]+1, uf.size[parent])
