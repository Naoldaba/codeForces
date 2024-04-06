test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    l = cnt = 0
    ind = 1
    r = 0
    while r < n:
        while l<=r and ind>arr[r]:
            l+=1
            ind-=1
        cnt+=(r-l+1)
        r+=1
        ind+=1

    print(cnt)



