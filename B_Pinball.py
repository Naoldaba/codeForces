test=int(input())

for _ in range(test):
    n=int(input())
    string=input()

    for i in range(n):
        st=list(string)
        ind=i
        ans=0
        while ind>=0 and ind<n:
            
            if st[ind]=='>':
                st[ind]='<'
                ind+=1
                
            else:
                st[ind]='>'
                ind-=1
            ans+=1
        print(ans, end=" ")
    print()