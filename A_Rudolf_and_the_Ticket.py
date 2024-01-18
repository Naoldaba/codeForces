test=int(input())
for _ in range(test):
    n,m,k=map(int, input().split())
    arr1=list(map(int, input().split()))
    arr2=list(map(int, input().split()))
    ways=0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]+arr2[j]<=k:
                ways+=1
    print(ways)
