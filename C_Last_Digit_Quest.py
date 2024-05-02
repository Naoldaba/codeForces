from collections import defaultdict

test=int(input())
for _ in range(test):
    n=int(input())
    Hash=defaultdict(int)
    res=0
    arr= list(map(int, input().split()))

    for i in range(n):
        dig=arr[i]%10
        Hash[dig]+=1

    for i in range(10):
        for j in range(10):
            for k in range(10):
                a1, a2, a3= -1, -1, -1
                if Hash[i]!=0:
                    a1=1
                    Hash[i]-=1
                if Hash[j]!=0:
                    a2=1
                    Hash[j]-=1
                if Hash[k]!=0:
                    a3=1
                    Hash[k]-=1
                if a1==1 and a2==1 and a3==1:
                    Sum=i+j+k
                    if Sum % 10==3:
                        res=1
                        break
                if a1==1:
                    Hash[i]+=1
                if a2==1:
                    Hash[j]+=1
                if a3==1:
                    Hash[k]+=1
            if res==1:
                break
        if res==1:
            break
    if res==1:
        print("YES")
    else:
        print("NO")
    
