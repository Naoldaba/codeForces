n=int(input())
ans=0

for j in range(1,n+1):
    d=2
    temp=set()
    i = j
    
    while d*d<=i:
        while i%d==0:
            temp.add(d)
            i//=d
        d+=1
    if i>1:
        temp.add(i)
    if len(temp)==2:
        ans+=1
print(ans)

