def mergeSort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=mergeSort(arr[:mid])
    right=mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    global ans
    Sorted=[]
    if left[0]<=right[0]:
        Sorted.extend(left+right)
    else:
        Sorted.extend(right+left)
        ans+=1
    return Sorted

test=int(input())
for _ in range(test):
    ans=0
    n=int(input())
    arr=list(map(int, input().split()))
    
    returned=mergeSort(arr)
    if returned!=sorted(arr):
        print(-1)
    else:
        print(ans)
