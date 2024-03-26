test=int(input())
for i in range(test):
    a, b= map(int,input().split())
    arr1=list(map(int, input().split(" ")))
    arr2=list(map(int, input().split(" ")))
    ans=0
    arr1=sorted(arr1, reverse=True)
    arr2=sorted(arr2)
    i=0
    while i< len(arr1):
        if abs(arr1[i]-arr2[i]) >=abs(arr1[-1]-arr2[-1]):
            ans+=abs(arr1[i]-arr2[i])
            i+=1
        else:
            ans+=abs(arr1[-1]-arr2[-1])
            arr1.pop()
            arr2.pop()
    print(ans)

        

    