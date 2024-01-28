test=int(input())
for _ in range(test):
    n, k = map(int, input().split())
    if n-k>=2:
        print(n)
    else:
        print(1)