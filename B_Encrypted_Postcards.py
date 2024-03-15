test_cases=int(input())
for k in range(test_cases):
    length=int(input())
    string=input()
    decrypt=""
    j=0
    i=1
    while i < length:
        if string[i]==string[j]:
            decrypt+=string[i]
            i+=2
            j=i-1
        else:
            i+=1
    print(decrypt)

