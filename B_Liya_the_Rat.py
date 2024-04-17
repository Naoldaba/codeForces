s=input()

n=int(input())
prefix=[0]
for i in range(len(s)):
    if s[i]==s[i-1]:
        prefix.append(prefix[-1]+1)
    else:
        prefix.append(prefix[-1])
    print(prefix)
for i in range(n):
    l, r=map(int, input().split())
    print(prefix[r]-prefix[l])

    
