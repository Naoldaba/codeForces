test=int(input())
for _ in range(test):
    str_len=int(input())
    string=input()
    vowel={"a","e"}
    cons={"b","d","c"}
    ans=[]
    i=0
    while i < str_len:
        if i+3<str_len and string[i+3] in cons:
            ans.append(string[i:i+3])
            i+=3
        elif i+3>=str_len:
            ans.append(string[i:])
            i=str_len
        else:
            ans.append(string[i:i+2])
            i+=2
        
    print('.'.join(ans))