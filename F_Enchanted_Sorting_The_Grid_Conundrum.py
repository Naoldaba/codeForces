t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    for row in grid:
        if sorted(row) == row:
            continue

        for i in range(1, m):
            if row[i] < row[i-1]:
                for j in range(i+1, m):
                    if row[j] < row[i-1]:
                        print(i, j)
                        break
                else:
                    print(-1)
                break
        break
    else:
        print(-1)