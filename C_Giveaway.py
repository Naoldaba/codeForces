test = 1
while test > 0:
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    b = [0] * (n+1)
    for i in range(1, n+1):
        b[i] = b[i-1] + a[i-1]

    while q > 0:
        x, y = map(int, input().split())
        y = x - y
        print(b[x] - b[y])
        q -= 1

    test -= 1