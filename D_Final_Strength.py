test=int(input())
for _ in range(test):
    n=int(input())
    strength=list(map(int, input().split()))

    for i in range(1, n+1):
        new_str=[]
        group=2**i
        for j in range(0, len(strength), group):
            group=strength[j:j+group]
            winner=[max(group[k], group[k+1]) for k in range(0, len(group), 2)]

            new_str.extend(winner)
            strength = [strength[k]+range(len(strength))]

            print(*strength)

        