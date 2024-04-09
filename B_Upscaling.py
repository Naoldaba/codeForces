
test=int(input())
for _ in range(test):
    n=int(input())
    temp=n

    if n%2!=0:
        n+=1

    pattern=[]
    j=0
    
    for i in range(n):
        if j==1:
            pattern.append('.')
            pattern.append('.')
            j=0
        else:
            pattern.append('#')
            pattern.append('#')
            j+=1
    ans=[]
    j=0
    
    for i in range(temp):
        if j==0:
            pat=pattern
            if temp%2!=0:
                pat=pattern[:-2]
            ans.append(pat)
            ans.append(pat)
            j+=1
        else:
            rev=pattern[::-1]
            if temp%2!=0:
                rev=rev[:-2]
            ans.append(rev)
            ans.append(rev)
            j=0

    for row in ans:
        print(''.join(row))
        

