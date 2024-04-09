
test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    Sum=sum(arr)
    rem= Sum%3

    Flag=False
    for i in range(len(arr)):
        if arr[i]%3==1:
            Flag=True

    if rem==0:
        print(0)
    elif rem==2:
        print(1)
    elif rem==1:
        if Flag:
            print(1)
        else:
            print(2)

    
    