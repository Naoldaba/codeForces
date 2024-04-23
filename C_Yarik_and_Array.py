
test=int(input())
for i in range(test):
    Len=int(input())
    arr=list(map(int, input().split()))
    Max=temp=arr[0]
    for r in range(1, Len):
        if abs(arr[r])%2==abs(arr[r-1])%2: 
            temp=arr[r]
        else:
            temp=max(arr[r], temp+arr[r])
        Max=max(Max, temp)
    print(Max)

        

