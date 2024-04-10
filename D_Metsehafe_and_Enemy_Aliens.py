t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    total_sum = sum(arr)

    ans = 0
    if total_sum % 2 != 0:
        ans += 1

    ans += total_sum // 2
    total_sum //= 2

    j = n - 1
    while total_sum > 0:
        total_sum -= arr[j]
        ans += 1
        j -= 1

    print(ans)
