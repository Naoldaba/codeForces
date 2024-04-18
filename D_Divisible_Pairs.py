t = int(input())

for _ in range(t):
    
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    sum_val = 0
    mp = {}

    for i in range(n):
        r = ((-a[i] % x) + x) % x
        s = a[i] % y

        sum_val += mp.get((r, s), 0)
        mp[(a[i] % x, a[i] % y)] = mp.get((a[i] % x, a[i] % y), 0) + 1

    print(sum_val)
