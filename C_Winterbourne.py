t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    total_required_chairs = sum(a)
    total_available_chairs = m - sum(a)

    possible = True
    for i in range(n):
        min_chair = (i - a[i]) % m
        max_chair = (i + a[i]) % m

  
        if min_chair <= max_chair:
            available_chairs = max_chair - min_chair
        else:
            available_chairs = m - (min_chair - max_chair)


        if min_chair == 0:
            available_chairs -= 1


        if available_chairs < a[i]:
            possible = False
            break


    if total_required_chairs > total_available_chairs:
        possible = False

    print("YES" if possible else "NO")
