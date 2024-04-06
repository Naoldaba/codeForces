test = int(input())
for _ in range(test):
    n, k = map(int, input().split())

    bits = [0] * 32
    arr = list(map(int, input().split()))
    for x in arr:
        j = 0
        while x:
            if x & 1:
                bits[j] += 1
            x >>= 1
            j += 1

    for i in range(30, -1, -1):
        if k >= n - bits[i]:
            k -= n - bits[i]
            bits[i] = n

    ans = 0
    for i in range(31):
        if bits[i] == n:
            ans += (1 << i)

    print(ans)