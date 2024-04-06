test=int(input())
for _ in range(test):
    n=int(input())
    s=input()
    i, j=0, len(s)-1
    while i<=j and s[i]!=s[j]:
        i+=1
        j-=1
    print(j-i+1)
