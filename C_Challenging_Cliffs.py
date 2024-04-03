n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    diff = float('inf')
    for i in range(size - 1):
        diff = min(diff, arr[i + 1] - arr[i])

    for i in range(size - 1):
        if arr[i + 1] - arr[i] == diff:
            print(arr[i], end=" ")
            for j in range(i + 2, size):
                print(arr[j], end=" ")
            for j in range(i):
                print(arr[j], end=" ")
            print(arr[i + 1])
            break

   