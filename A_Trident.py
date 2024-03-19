test=int(input())
for _ in range(test):
    n=int(input())
    arr=list(map(int, input().split()))
    flag=0
    for i in range(1, n-1):
        if arr[i-1] < arr[i] and arr[i]> arr[i+1]:
            flag=1
            break
        
    if not flag:
        print("NO")
    else:
        print("YES")
        print(i, i+1, i+2)


