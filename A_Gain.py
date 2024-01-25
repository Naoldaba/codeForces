test=int(input())
for i in range(test):
    n=int(input())
    arr=list(map(int, input().split()))
    ans=[0]*n
    arr_sorted=sorted(arr)
    Max=arr_sorted[-1]
    for i in range(n):
        if arr[i]!=Max:
            ans[i]=arr[i]-Max
        else:
            if len(arr)>1:
                ans[i]=arr[i]-arr_sorted[-2]

    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()