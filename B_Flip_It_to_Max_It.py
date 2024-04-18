test=int(input())

for i in range(test):
    arr_len=int(input())
    arr=list(map(int, input().split(" ")))

    total=0
    flag=False
    ops=0

    for i in range(arr_len):
        total+=abs(arr[i])
    
    for i in range(arr_len):
        if arr[i]==0:
            continue
        if arr[i]<0:
            flag=True
        else:
            if flag==True:
                ops+=1
                flag=False
    if flag:
        ops+=1

    print(total, ops)
        
    
        