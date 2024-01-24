test = int(input())

for _ in range(test):
    n, d =map(int, input().split())
    number = input()
    ans = ""

    len = -1
    for i in range(n):
        if number[i] < str(d):
            len = i
            break

    if len == -1:
        ans = number + str(d)
    else:
        ans = number[:len] + str(d) + number[len:]

    print(ans)