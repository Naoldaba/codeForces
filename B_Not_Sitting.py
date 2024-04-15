t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    allDist = []

    for i in range(n):
        for j in range(m):
            d1 = i + j
            d2 = i + (m - j - 1)
            d3 = (n - i - 1) + j
            d4 = (n - i - 1) + (m - j - 1)
            allDist.append(max(d1, d2, d3, d4))

    allDist.sort()

    for i in range(n * m):
        print(allDist[i], end=" ")

    print()