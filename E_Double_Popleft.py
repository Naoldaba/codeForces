from collections import deque

n, queries= map(int, input().split())
arr=list(map(int, input().split()))

arr=deque(arr)

for i in range(queries):
    q=int(input())
    print(arr[0], arr[1])
    for i in range(q):
        # print(arr)
        a=arr.popleft()
        b=arr.popleft()
        if a>b:
            arr.appendleft(a)
            arr.append(b)
        else:
            arr.appendleft(b)
            arr.append(a)
        # print(a, b)
    

