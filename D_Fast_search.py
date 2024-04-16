
n=int(input())
arr=list(map(int, input().split()))
arr.sort()
k=int(input())
ans=[]
for _ in range(k):
    l_bound, r_bound=map(int, input().split())

    l,r=0, len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>=l_bound:
            r=mid-1
        else:
            l=mid+1
    L_ind=l

    l,r=0, len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]<=r_bound:
            l=mid+1
        else:
            r=mid-1
    R_ind=l

    ans.append(R_ind-L_ind)

print(*ans)

