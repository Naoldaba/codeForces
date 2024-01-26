query = int(input())

for _ in range(query):
    n, k = map(int, input().split())
    ans=0
    while n>0:
        rem=n%k
        if n%k==0:
            n//=k
            ans+=1
        else:
            n-=rem
            ans+=rem
    print(ans)