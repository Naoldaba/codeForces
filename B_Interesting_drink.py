n=int(input())
arr=list(map(int, input().split()))

days=int(input())
day_arr=[]
for i in range(days):
    coin=int(input())
    day_arr.append(coin)

arr.sort()

for i in range(len(day_arr)):
    l, r = 0, len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]<=day_arr[i]:
            l=mid+1
        else:
            r=mid-1
    print(l)
