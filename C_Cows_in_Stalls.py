
n, k = map(int, input().split())
stalls = list(map(int, input().split()))

stalls.sort()
left, right = 1, stalls[-1]-stalls[0]+1

ans=left
while left<=right:
    mid=(left+right)//2
    last_pos=stalls[0]
    count=1
    for i in range(1, n):
        if stalls[i]-last_pos>=mid:
            count+=1
            last_pos=stalls[i]
    if count>=k:
        ans=max(ans, mid)
        left=mid+1
    else:
        right=mid-1
print(ans)
