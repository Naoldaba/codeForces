from collections import deque

test=int(input())
for _ in range(test):
    n,m,x=map(int, input().split())
    arr=[]
    for i in range(m):
        temp=list(input().split())
        arr.append(temp)
    Set={x}
    for r, d in arr:
        if d=='0':
            temp_set=set()
            for i in Set:
                p1=i+int(r)
                if p1>n:
                    p1-=n
                temp_set.add(p1)
            Set=temp_set

        elif d=='1':
            temp_set=set()
            for i in Set:
                p2=i-int(r)+n
                if p2>n:
                    p2-=n
                temp_set.add(p2)
            Set=temp_set
        else:
            temp_set=set()
            for i in Set:
                p1=i+int(r)
                if p1>n:
                    p1-=n
                temp_set.add(p1)

                p2=i-int(r)+n
                if p2>n:
                    p2-=n
                temp_set.add(p2)
            Set=temp_set
        
    ans=list(Set)
    ans.sort()
    print(len(Set))
    print(*ans)
            
    
