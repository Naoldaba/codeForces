from collections import defaultdict

n = int(input())
s = input()

dic=defaultdict(int)
types = 0
left = 0
right = 0
minFlats = float('inf')
unique=set(s)

for right in range(n):
    dic[s[right]]+=1

    while len(dic)==len(unique):
        minFlats=min(minFlats, right-left+1)

        dic[s[left]]-=1
        if dic[s[left]]<=0:
            del dic[s[left]]
        left+=1
    

print(minFlats)