t = int(input())

for _ in range(t):
    n = int(input())
    periods = list(map(int, input().split()))

    lcm = periods[0]
    for i in range(1, n):
        # Compute the least common multiple of the current LCM and the next period
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def lcm_func(a, b):
            return a * b // gcd(a, b)
        
        lcm = lcm_func(lcm, periods[i])

    print(lcm)
