test=int(input())
for i in range(test):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    if i!=test-1:
        empty=input()
    flag=True
    
    for i in range(n-1, -1,-1):
        if a[i]+b[n-i-1]>k:
            flag=False
            break
        
    print("Yes") if flag else print("No")