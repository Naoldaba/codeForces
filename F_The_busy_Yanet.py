test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    index = 0
    Min=min(arr)

    for i in range(n):
        if arr[i] == Min:
            index = i
            break

    if sorted(arr[index:]) == arr[index:]:
        print(index)
    else:
        print(-1)

