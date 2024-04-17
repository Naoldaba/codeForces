test=int(input())
for i in range(test):
    n=int(input())
    arr=list(map(int, input().split()))
    cum=0
    flag=True
    target=sum(arr)//n
    for i in range(n):
        if cum<0:
            flag=False
        if arr[i] > target:
            cum+=arr[i]-target
        elif arr[i]<target:
            cum-=target-arr[i]
    print("YES") if flag else print("NO")
