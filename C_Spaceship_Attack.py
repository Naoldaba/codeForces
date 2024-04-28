from collections import defaultdict

s,b = map(int, input().split())
attacking_power=list(map(int, input().split()))
pairs=[]
for i in range(b):
    pair=list(map(int, input().split()))
    pairs.append(pair)

pairs.sort()
cum_gold=[0]*(b+1)
for i in range(1, b+1):
    cum_gold[i]=cum_gold[i-1]+pairs[i-1][1]

gold=[]
for ships in attacking_power:
    left, right=0, b-1
    while left<=right: 
        mid=(left+right)//2
        if pairs[mid][0]<=ships:
            left=mid+1
        else:
            right=mid-1
    gold.append(cum_gold[left])
print(*gold)






