test=int(input())

for _ in range(test):
    n=int(input())
    if n%2==0:
        for i in range(n, 0, -1):
            print(i, end=" ")
        print()

    else:
        if n==3:
            print(-1)

        else:
            fixed=(n+1)//2
            ind=1
            for i in range(n, 0, -1):
                if i>fixed:
                    print(i, end=" ")
                else:
                    print(ind, end=" ")
                    ind+=1
            print()
    
