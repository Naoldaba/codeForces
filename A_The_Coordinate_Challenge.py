test= int(input())
for _ in range(test):
    n=int(input())
    if n==1:
        print(2)
    elif n%3==0:
        print(n//3)
    else:
        print((n//3)+1)
    
    