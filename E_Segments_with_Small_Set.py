from collections import defaultdict;

n,k=map(int, input().split())
arr=list(map(int, input().split()))

left=0
distinct_elements=0
freq=defaultdict(int)
ans=0

for right in range(n):
    if arr[right] not in freq or freq[arr[right]]==0:
        distinct_elements+=1
    freq[arr[right]]+=1

    while distinct_elements>k:
        freq[arr[left]]-=1
        if freq[arr[left]]==0:
            distinct_elements-=1
        left+=1
    ans+= right-left+1
print(ans)

    
