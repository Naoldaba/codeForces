import math

w, h, n= map(int, input().split())

left, right= max(w,h), max(w*n, h*n)
ans=right
while left<=right:
    mid=(left+right)//2
    if ((mid//w)*(mid//h)) >= n:
        ans=min(ans, mid)
        right=mid-1
    else:
        left=mid+1
print(ans)
