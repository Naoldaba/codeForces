n=int(input())
arr=list(map(int, input().split()))
arr.sort()
count=0
prefix=[0]
for i in range(n):
    if prefix[-1] > arr[i]:
        prefix.append(prefix[-1])
    else:
        prefix.append(prefix[-1]+arr[i])

for i in range(n):
    if arr[i]>=prefix[i]:
        count+=1
print(count)