
test=int(input())
for _ in range(test):
    n=int(input())
    arr=list(map(int, input().split()))

    arr.sort()
    count=0
    mid=len(arr)//2
    if len(arr)%2==0:
        mid-=1
    i=mid
    while i<len(arr) and arr[i]==arr[mid]:
        count+=1
        i+=1
        
    print(count)


