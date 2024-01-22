t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    pos = [[] for _ in range(n + 2)]

    for i in range(1, n + 1):
        pos[a[i-1]].append(i)

    l = 1
    b = []

    while l <= n:
        mex = 0
        r = l

        for mex in range(n + 2):
            it = next((x for x in pos[mex] if x >= l), None)

            if it is None:
                break

            r = max(r, it)

        b.append(mex)
        l = r + 1

    print(len(b))
    print(' '.join(map(str, b)))