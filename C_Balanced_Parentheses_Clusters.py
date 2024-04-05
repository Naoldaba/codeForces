
class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.parent[root_x]<self.parent[root_y]:
                self.parent[root_y]=root_x
            else:
                self.parent[root_x]=root_y
    
test = int(input())

for _ in range(test):
    n = int(input())
    s = input()
    stack=[]

    uf = UnionFind(2 * n)

    for i, c in enumerate(s):
        if c=='(':
            if i-1>=0 and s[i-1]==')':
                uf.union(i-1, i)
            stack.append(i)

        else:
            uf.union(i, stack.pop())

    comps=set()

    for i in range(len(s)):
        comps.add(uf.find(i))

    print(len(comps))
        

    
    