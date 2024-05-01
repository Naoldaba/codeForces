t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    i=0
    j=n-1
    ans=float('inf')

    while j>=0 and arr[j]==arr[n-1]:
        j-=1
    while i<n and arr[i]==arr[n-1]:
        i+=1
    
    if j<i:
        ans=0
    else:
        ans= min(ans, j-i+1)

    i=0
    j=n-1

    while i<n and arr[i]==arr[0]:
        i+=1
    while j>=0 and arr[j]==arr[0]:
        j-=1

    if j<i:
        ans=0
    else:
        ans=min(ans, j-i+1)

    print(ans)
