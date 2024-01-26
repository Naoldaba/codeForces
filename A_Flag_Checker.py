n, m = map(int, input().split())
flag = [input() for _ in range(n)]

Flag = True

for row in flag:
    if len(set(row)) > 1:
        Flag = False
        break

for i in range(1, n):
    if flag[i] == flag[i-1]:
        Flag = False
        break

if Flag:
    print("YES")
else:
    print("NO")