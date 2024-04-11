test = int(input())

for _ in range(test):
    num = int(input())
    if (num & (num - 1)) == 0:
        print("NO")
    else:
        print("YES")