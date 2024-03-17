n, t = map(int, input().split())

arr=list(map(int, input().split()))

l=total=0
Max=0

for r in range(len(arr)):
    total+=arr[r]
    while total>t:
        total-=arr[l]
        l+=1
    Max=max(Max, r-l+1)
print(Max)
    

