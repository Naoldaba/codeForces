test = int(input())

for _ in range(test):
    a, b, c = map(int, input().split())

    ans=a
    r=b%3
    if r==0:
        ans+=b//3
        ans+=c//3 if c%3==0 else c//3 + 1
        print(ans)
    elif (c>=3-r):
        b+=3-r
        c-=3-r
        ans+=b//3
        ans+=c//3 if c%3==0 else c//3 +1
        print(ans)
    else:
        print(-1)

            

    
    
    

    
