test = int(input())

for _ in range(test):

    n=int(input())
    arr=[10,11]
    i=0
    while i<len(arr):
        num1=arr[i]*10
        num2=num1+1

        if num1<=n:
            arr.append(num1)
        if num2<=n:
            arr.append(num2)

        i+=1

    arr.sort(reverse=True)

    for i in range(len(arr)):
        while n%arr[i]==0:
            n//=arr[i]
        if n==1:
            break

    print("YES") if n==1 else print("NO")
        
    


