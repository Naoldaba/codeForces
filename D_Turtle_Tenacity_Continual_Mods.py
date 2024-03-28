test=int(input())
for i in range(test):
    n=int(input())
    arr=list(map(int, input().split()))

    arr.sort(reverse=True)
    Mod=arr[1]%arr[0]
    for i in range(2,len(arr)):
        if Mod==0:
            break
        if arr[i]<=Mod:
            print("NO")
            break
    print("YES")


