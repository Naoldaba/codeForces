from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent={i:i for i in range(n)}
        self.size=[1]*n

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
                self.size[root_y]+=self.size[root_x]
            else:
                self.parent[root_y]=root_x
                self.size[root_x]+=self.size[root_y]


n, m, k = map(int, input().split())
graph=defaultdict(set)
uf=UnionFind(n)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].add(v-1)
    graph[v-1].add(u-1)

queries=[]
for _ in range(k):
    query=input().split()
    queries.append(query)

result=[]
for query in queries[::-1]:
    node1=int(query[1])-1
    node2=int(query[2])-1

    if query[0]=="ask":
        if uf.find(node1)==uf.find(node2):
            result.append("YES")
        else:
            result.append("NO")

    else:
        uf.union(node1, node2)

for _ in range(len(result)):
    print(result.pop())
        


        

        



