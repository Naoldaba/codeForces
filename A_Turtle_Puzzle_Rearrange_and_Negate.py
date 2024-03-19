test=int(input())
for i in range(test):
    n=int(input())
    arr=list(map(int, input().split()))
    Sum=sum(arr)
    Max=Sum
    Sorted_arr=sorted(arr)
    for i in range(len(Sorted_arr)):
        if Sorted_arr[i]<0:
            Sorted_arr[i]=abs(Sorted_arr[i])
    Max=max(Max, sum(Sorted_arr))
    print(Max)