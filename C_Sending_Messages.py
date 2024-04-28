test=int(input())
for i in range(test):
    n,f,a,b= map(int, input().split(" "))
    arr=list(map(int, input().split(" ")))
    status=False
    init_mom=0
    for i in range(len(arr)):
        opt=min(b, (arr[i]-init_mom)*a)
        f-=opt
        if f <=0:
            print("NO")
            status=True
            break
        
        init_mom=arr[i]
    if not status:
        print("YES")
