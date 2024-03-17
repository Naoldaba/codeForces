test=int(input())
for i in range(test):
    n=int(input())
    flag=True
    arr=list(map(int, input().split()))
    arr.sort()
    if arr[0]!=1:
        flag=False
    else:
        prefix=1
        for i in range(1,n):
            if arr[i]>prefix:
                flag=False
                break
            prefix+=arr[i]
    print("YES") if flag==True else print("NO")
    