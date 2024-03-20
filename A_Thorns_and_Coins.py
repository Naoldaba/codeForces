test=int(input())
for _ in range(test):
    n=int(input())
    string=input()
    i=0
    count=0
    flag=True
    while i<len(string)-1 :
        if string[i+1]!="*":
            if string[i+1]=="@":
                count+=1
            i+=1
        elif i+2<len(string) and string[i+2]!="*":
            if string[i+2]=="@":
                count+=1
            i+=2
        else:
            flag=False
            break
    print(count)


