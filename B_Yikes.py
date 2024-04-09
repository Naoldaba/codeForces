n=int(input())
arr=list(map(int, input().split()))

prefix_arr=[0]
for i in range(len(arr)):
    prefix_arr.append(prefix_arr[-1]+arr[i])

num_q=int(input())
queries=list(map(int, input().split()))


for query in queries:
    l, r= 0, len(prefix_arr)
    while l<=r:
        mid=(l+r)//2
        if prefix_arr[mid]>=query:
            r=mid-1
        else:
            l=mid+1
    print(l)
    
