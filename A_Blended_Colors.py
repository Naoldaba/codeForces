test = int(input())

for _ in range(test):
    n = int(input())
    row1 = input().replace('G', 'B')
    row2 = input().replace('G', 'B')

    if row1 == row2:
        print("YES")
    else:
        print("NO")