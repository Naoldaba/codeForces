test=int(input())
for _ in range(test):
    n=int(input())
    s=input()
    count=0
    if len(s)<3:
        print(count)
    else:
        i=0
        while i<len(s)-2:
            if s[i]=='m' and s[i+1]=='a' and s[i+2]=='p':
                count+=1
                i+=3
            elif s[i]=='p' and s[i+1]=='i' and s[i+2]=='e':
                count+=1
                i+=3
            else:
                i+=1
        print(count)

            
