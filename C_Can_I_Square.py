import math
test=int(input())
for _ in range(test):
    buckets=int(input())
    row=list(map(int, input().split(" ")))
    # print(row)
    Sum=sum(row)
    # print(Sum)
    if math.sqrt(Sum).is_integer():
        print("YES")
    else:
        print("NO")
