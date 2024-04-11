from collections import defaultdict
import math
arr_len=int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

dic = defaultdict(int)
result=0
for i in range(len(arr1)):
    if arr1[i] == 0:
        if arr2[i]==0:
            result+=1
    else:
        nomin=arr1[i]//(math.gcd(abs(arr1[i]), abs(arr2[i])))
        denom=arr2[i]//(math.gcd(abs(arr1[i]), abs(arr2[i])))

        if arr2[i]<0:
            nomin*=-1
            denom*=-1
        elif arr2[i]==0 and arr1[i]<0:
            denom*=-1
        dic[(nomin, denom)]+=1
if len(dic)==0:
    print(result)
else:
    print(result+max(dic.values()))

        