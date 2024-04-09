test = int(input())

for _ in range(test):
    n, z = map(int, input().split())
    arr = list(map(int, input().split()))
    Max = max(arr)
    for i in range(n):
        arr[i] = arr[i] | z
        z = arr[i] & z
    Max = max(Max, max(arr))

    print(Max)