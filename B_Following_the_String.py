test = int(input())
for i in range(test):
    n = int(input())
    ans = ""
    frq = [-1] * 26
    ar = list(map(int, input().split()))
    for i in range(n):
        for k in range(25, -1, -1):
            if frq[k] == ar[i] - 1:
                frq[k] += 1
                ans += chr(k + ord('a'))
                break
    print(ans)
