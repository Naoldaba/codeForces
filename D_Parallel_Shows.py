shows=int(input())
arr=[]
for i in range(shows):
    show=list(map(int, input().split()))
    arr.append(show)

num_of_tv=1
for i in range(1,len(arr)):
    if arr[i][0]<=arr[i-1][1]:
        num_of_tv+=1
print("YES") if num_of_tv<=2 else print("NO")

