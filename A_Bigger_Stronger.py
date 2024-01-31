
t = int(input())
for _ in range(t):
    
    n = int(input())
    arr = list(map(int, input().split()))

   
    arr.sort()
    is_possible = all(arr[i] < arr[i + 1] for i in range(n - 1))
    
    if is_possible:
        print("YES")
    else:
        print("NO")
