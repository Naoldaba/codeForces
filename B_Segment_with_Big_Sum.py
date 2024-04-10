n,s=map(int, input().split())
arr=list(map(int, input().split()))
l=0
Sum=0
Len=float('inf')
for r in range(n):
    Sum+=arr[r]
    while Sum>=s:
        Sum-=arr[l]
        Len=min(Len, r-l+1)
        l+=1
        
if Len!=float('inf'):
    print(Len)
else:
    print(-1)


