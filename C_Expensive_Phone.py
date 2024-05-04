test=int(input())
for _ in range(test):
    n=int(input())
    stack=[]
    arr=list(map(int, input().split()))
    cnt=0
    
    for i in range(len(arr)):
        while stack and stack[-1]>arr[i]:
            cnt+=1
            stack.pop()
        stack.append(arr[i])
    else:
        print(cnt)


