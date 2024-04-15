test = int(input())

for _ in range(test):
    n = int(input())
    s = list(input().strip())
    
    l, r = -1, -1
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if l == -1:
                l = i
            r = i

    if l != -1:
        for i in range(l, r + 1):
            s[i] = '0' if s[i] == '1' else '1'

    is_p = all(s[i] == s[n - i - 1] for i in range(n // 2))

    if is_p:
        print("Yes")
    else:
        print("No")
