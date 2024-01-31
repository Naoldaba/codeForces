n, k= map(int, input().split())

arr=list(map(int, input().split()))
queries=list(map(int, input().split()))
# print(queries)


for query in queries:
    l, r = 0, len(arr)-1
    flag=False
    while l<=r:
        mid=(l+r)//2

        if arr[mid]==query:
            flag=True
            break
        elif arr[mid]>query:
            r=mid-1
        else:
            l=mid+1
    print("YES") if flag else print("NO")