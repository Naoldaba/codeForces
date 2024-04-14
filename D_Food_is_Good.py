test = int(input())
for i in range(test):
    n=int(input())
    arr=list(map(int, input().split()))
    simon_taste=sum(arr)
    prefix=[0]
    for i in range(len(arr)):
        prefix.append(prefix[-1]+arr[i])
    # 0-n-1
    Aman_taste=temp=arr[0]
    for i in range(1, len(arr)-1):
        temp=max(temp, arr[i]+temp)
        Aman_taste=max(Aman_taste, temp)
    # 1-n
    temp=arr[1]
    for i in range(2,len(arr)):
        temp=max(temp, arr[i]+temp)
        Aman_taste=max(Aman_taste, temp)
    if Aman_taste < simon_taste:
        print("YES")
    else:
        print("NO")

# test=int(input())
# for i in range(test):
#     n=int(input())
#     arr=list(map(int, input().split()))
#     l_sum=r_sum=0
#     flag=0
#     for i in range(len(arr)):
#         l_sum+=arr[i]
#         r_sum+=arr[n-1-i]
#         if (l_sum<=0 or r_sum<=0):
#             flag=1
#             break
#     if flag:
#         print("NO")
#     else:
#         print("YES")

