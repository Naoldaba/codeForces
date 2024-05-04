n = int(input())
ans = 0
arr = list(map(int, input().split()))
arr_count = [0] * 1001

for x in arr:
    arr_count[x] += 1

for _ in range(n):
    flag = False
    for j in range(1, 1001):
        if arr_count[j]:
            if flag:
                ans += 1
            arr_count[j] -= 1
            flag = True

print(ans)
