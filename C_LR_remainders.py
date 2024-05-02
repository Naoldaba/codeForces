test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    string = input()

    prefix = 1
    for num in arr:
        prefix *= num

    ans = []
    l = 0
    r = 0

    for char in string:
        ans.append(prefix % m)
        if char == "L":
            prefix //= arr[l]
            l += 1
        else:
            prefix //= arr[n - r - 1]
            r += 1

    print(*ans)
