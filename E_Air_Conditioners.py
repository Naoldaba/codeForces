test=int(input())
empty=input()

for j in range(test):
    
    n, k = map(int, input().split())
    arr=[float('inf')]*n
    k_pos=list(map(int, input().split()))
    k_val=list(map(int, input().split()))

    if j != test-1:
        none = input()
    
    for i in range(k):
        arr[k_pos[i]-1] = k_val[i]
    

    prefix=[0] * n
    suffix=[0] * n
    temp=float('inf')

    for i in range(n):
        temp = min(arr[i], temp+1)
        prefix[i] = temp

    temp = float('inf')
    for j in range(n-1, -1, -1):
        temp= min(temp+1, arr[j])
        suffix[j]=temp

    for i in range(n):
        arr[i] = min(prefix[i], suffix[i])
        
    print(*arr)

    


    

