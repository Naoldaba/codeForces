# from collections import Counter

# test = int(input())

# for _ in range(test):
#     n = int(input())
#     arr = list(map(int, input().split()))

#     count=Counter(arr)
#     Sorted=sorted(count.values(), reverse=True)
    
#     ans=prev=Sorted[0]

#     for i in range(1, len(Sorted)):
#         if prev==0:
#             break
#         if Sorted[i]>=prev:
#             prev-=1
#             ans+=prev
#         else:
#             prev=Sorted[i]
#             ans+=prev
#     print(ans)


test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    freq=[0]*n
    for i in range(len(arr)):
        freq[arr[i]-1]+=1

    freq.sort()
    
    for i in range(len(freq)-2,-1,-1):
        if freq[i]>=freq[i+1]:
            freq[i]=max(freq[i+1]-1, 0)

    ans= sum(freq)

    print(ans)

    
