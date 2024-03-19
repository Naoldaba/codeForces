
test=int(input())
for _ in range(test):
    a, b=map(int, input().split())
    if a==b:
        print("Bob")
    else:
        if abs(a-b)%2==0:
            print("Bob")
        else:
            print("Alice")