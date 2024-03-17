
test=int(input())
for _ in range(test):
    n=int(input())
    arr=list(map(int, input().split()))
    flag=True
    last=0

    for i in range(n):
        if arr[i] >= last:
            if arr[i]>=10:
                x,y=map(int, list(str(arr[i])))
                if last<=x<=y:
                    last=y
                else:
                    last=arr[i]
            else:
                last=arr[i]
        else:
            flag=False
            break

        
    print("YES") if flag else print("NO")




