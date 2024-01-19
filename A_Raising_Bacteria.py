num= int(input())
ans=0
while num:
    if num & 1:
        ans+=1
    num>>=1
print(ans)