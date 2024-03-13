def fun(ch, n, arr, tot):
    v = []
    for i in range(n):
        v.append(arr[i][ch] - (tot[i] - arr[i][ch]))
    v.sort(reverse=True)
    count = 0
    curr = 0
    for x in v:
        curr += x
        if curr > 0:
            count += 1
    return count

def solve():
    n = int(input())
    arr = [[0 for _ in range(5)] for _ in range(n)]
    tot = [0 for _ in range(n)]

    for i in range(n):
        s = input()
        tot[i] = len(s)
        for j in range(len(s)):
            arr[i][ord(s[j]) - ord('a')] += 1

    ans = 0
    for i in range(5):
        ans = max(ans, fun(i, n, arr, tot))
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
