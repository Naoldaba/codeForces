arr_len = int(input())
arr = list(map(int, input().split()))
flag = True
rem = 0

for i in range(arr_len):
    cur = arr[i]
    while cur % 2 == 0:
        cur //= 2
    while cur % 3 == 0:
        cur //= 3
    if i == 0:
        rem = cur
    elif rem != cur:
        flag = False
        break

print("Yes" if flag else "No")
