from collections import Counter

test= int(input())
for _ in range(test):
    n=int(input())
    arr=list(map(int, input().split()))

    if len(arr)==1:
        print(-1)

    else:
        count=Counter(arr)
        if len(count)==1:
            print(-1)
        else:
            result=len(arr)
            pointer=0
            for i in range(len(arr)):

                if arr[i]==arr[0]:
                    pointer+=1

                else:
                    result=min(result, pointer)
                    pointer=0
                    
            result=min(result, pointer)
            print(result)




