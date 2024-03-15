from collections import defaultdict, deque

test=int(input())
for _ in range(test):

    n, m = map(int, input().split())
    graph=defaultdict(list)
    indgre=[0]*n
    edges=[]
    for _ in range(m):
        t, x, y = map(int, input().split())
        x, y = x-1, y-1
        edges.append((x,y))
        if t==1:
            graph[x].append(y)

    for i in range(n):
        for node in graph[i]:
            indgre[node]+=1
    
    queue=deque()
    for i in range(n):
        if indgre[i]==0:
            queue.append(i)

    pos=[]
    while queue:
        curr= queue.popleft()
        pos.append(curr)
        for i in graph[curr]:
            indgre[i]-=1
            if indgre[i]==0:
                queue.append(i)

    if len(pos)!=n:
        print("NO")
    else:
        print("YES")
        ind=[-1]*n
        for i in range(n):
            ind[pos[i]]=i
        for u, v in edges:
            if ind[v]<ind[u]:
                print(v, u)
            else:
                print(u, v)
    
    

