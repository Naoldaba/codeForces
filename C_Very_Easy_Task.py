
n,x,y=map(int, input().split())

def check(time):
    copies=time//x + (time-x)//y
    return copies>=n

left, right = 1, max(x,y)*n

if y<x:
    x,y=y,x
    
ans=right
while left<=right:
    mid=(left+right)//2
    if check(mid):
        ans=min(ans, mid)
        right=mid-1
    else:
        left=mid+1
print(ans)
