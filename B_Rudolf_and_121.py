t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    flag=True
    for i in range(len(arr)-2):
        cur=arr[i]
        if cur<0:
            flag=False
            break
        arr[i]=0
        arr[i+1]-=2*cur
        arr[i+2]-=cur
    for i in range(len(arr)):
        if arr[i]!=0:
            flag=False
            break
    print("YES") if flag else print("NO")
