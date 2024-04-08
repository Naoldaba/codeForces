n,s=map(int, input().split())
arr=list(map(int, input().split()))
Sum=0
count=0
l=0
for r in range(n):
    Sum+=arr[r]
    count+=l
    while Sum>=s:
        Sum-=arr[l]
        count+=1
        l+=1
print(count)
