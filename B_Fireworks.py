import math

test=int(input())
for _ in range(test):
    a, b, m = map(int, input().split())

    if m < a and m < b:
        print(2)
    else:
        print((m//a)+(m//b)+2)