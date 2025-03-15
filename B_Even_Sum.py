t =int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    tot = sum(a)
    if tot%2 == 0:
        print(0)
        continue

    res = float('inf')
    for x in a:
        temp = 0
        while x%2 == (x//2) %2:
            temp += 1
            x //= 2
        res = min(res, temp+1)
    
    print(res)