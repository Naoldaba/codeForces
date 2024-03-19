test = int(input())

for _ in range(test):
    n, x = map(int, input().split())

    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    teams = 0
    count = 0
    for i in range(n):
        count += 1
        if arr[i] * count >= x:
            teams += 1
            count = 0

    print(teams)