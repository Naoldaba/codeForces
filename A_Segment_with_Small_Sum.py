n,s=map(int, input().split())
arr=list(map(int, input().split()))

Sum=0
l=0
Max=0
for r in range(len(arr)):
    Sum+=arr[r]
    while Sum>s:
        Sum-=arr[l]
        l+=1
    Max=max(Max, r-l+1)
print(Max)
    
