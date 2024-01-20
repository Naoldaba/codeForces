t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    Min_repaint=(n-((n//m)+(n%m!=0)))
    if Min_repaint<=k:
        print("NO")
    else:
        print("YES")