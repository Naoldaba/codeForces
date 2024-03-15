import math
test=int(input())
for _ in range(test):
    n, k =map(int, input().split())
    demand=list(map(int, input().split()))
    time=list(map(int, input().split()))

    l, r = 1, max(demand)
    
    def check(wagon):
        total_time=0
        for i in range(len(demand)):
            
            total_time+=time[i]*math.ceil(demand[i]/wagon)
        return total_time<=k
    flag=False
    while l<=r:
        mid=(l+r)//2
        if check(mid):
            flag=True
            r=mid-1
        else:
            l=mid+1
    print(l) if flag else print(-1)