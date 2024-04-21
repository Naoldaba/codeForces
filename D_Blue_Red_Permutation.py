t = int(input())

while t > 0:
    t -= 1
    n = int(input())

    arr = [0] + list(map(int, input().split()))

    colors = input()

    blue = []
    red = []

    for i in range(1, n + 1):
        if colors[i - 1] == 'B':
            blue.append(arr[i])
        else:
            red.append(arr[i])

    cur = 1

    blue.sort()
    red.sort()

    is_valid = True

    for i in blue:
        if i >= cur:
            cur += 1
        else:
            is_valid = False
            break

    for i in red:
        if i <= cur:
            cur += 1
        else:
            is_valid = False
            break

    print("YES" if is_valid else "NO")